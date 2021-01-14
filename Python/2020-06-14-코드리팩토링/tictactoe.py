import pickle
import copy
from tqdm import tqdm
import numpy as np
import random
import itertools

class Environment():
   
    def __init__(self):
        self.boardA = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.done = False
        self.reward = 0
        self.winner = 0
        self.turn = 1
        self.print = False

    def move(self, action):      
        self.boardA[action] = self.turn
        self.turn = self.turn % 2 + 1
        self.done, self.winner = end_check(self.boardA)
        if self.done and self.winner == 1: self.reward = 1
        if self.done and self.winner == 2: self.reward = -1
        if self.done and self.winner == 0: self.reward = 0

        return self.boardA, self.done, self.reward, self.winner

    def printBoard(self):
        print("===========")
        for i in range(3):
            for j in range(3):
                if self.boardA[3 * i + j] == 0:
                    print("|   ",end=" ")
                elif self.boardA[3 * i + j] == 1:
                    print("|  O",end=" ")
                elif self.boardA[3 * i + j] == 2:
                    print("|  X",end=" ")
            print("|")
            print("===========")
            
    def reset_board(self):
        self.boardA = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.turn = 1

class Policy_iteration_player():
    def __init__(self, restore=False):
        self.name = "Policy Iteration player"
        self._vtable = dict()
        self._policy = dict()
        if restore:
            self.dataRestore()
        else:
            self.initValue()
        #if not restore:
            #self.initValue()
        #else:
            #self.dataRestore()

    def initValue(self):
        boardA_list = itertools.product([0, 1, 2], repeat=9)
        for boardA in boardA_list:
            boardA = list(boardA)
            converted = convert(boardA)
            done, winner = end_check(boardA)
            if not done:
                self._vtable[converted] = random.uniform(-0.5, 0.5)
                self._policy[converted] = random.choice(get_action(boardA))
            else:
                self._vtable[converted] = 0
                
    def dataSave(self):
        file = open("save_policy.dat", 'wb')
        pickle.dump(self._vtable, file)
        file = open("save_policy.dat", 'wb')
        pickle.dump(self._policy, file)

    def vtable(self, boardA):
        converted = convert(boardA)
        return self._vtable[converted]

    def dataRestore(self):
        file = open("save_value.dat", 'rb')
        self._vtable = pickle.load(file)
        file = open("save_policy.dat", 'rb')
        self._policy = pickle.load(file)

    def learnVtable(self, boardA, x):
        converted = convert(boardA)
        self._vtable[converted] = x

    def selectAction(self, boardA):
        converted = convert(boardA)
        return self._policy[converted]

    def learnPolicy(self, boardA, x):
        converted = convert(boardA)
        self._policy[converted] = x

class policyIterationPlayerBase():
    def selectAction(self, boardA, turn):
        available_action = get_action(boardA)
        action_list = []

        for i in available_action:
            boardA[i] = turn
            done, winner = end_check(boardA)
            boardA[i] = 0
            if done:
                action_list.append(i)
        if len(action_list) == 0:
            action_list = available_action

        return random.choice(action_list)

class Human_player():
    def __init__(self):
        self.name = "Human player"
       
    def selectAction(self, boardA):
       
        while True:

            available_action = get_action(boardA)
            print("possible actions = {}".format(available_action))
           
            print("===========")
            print("+  0 +  1 +  2 +")
            print("===========")
            print("+  3 +  4 +  5 +")
            print("===========")
            print("+  6 +  7 +  8 +")
            print("===========")
           
            action = int(input("Select action(human) : "))
            if action in available_action:
                return action
            else:
                print("You selected wrong action")
        return




def get_action(boardA):
    observation = []
    for i in range(9):
        if boardA[i] == 0:
            observation.append(i)
    return observation


def end_check(boardA):
    for i in range(3):
        if boardA[3 * i] == boardA[3 * i + 1] and boardA[3 * i + 1] == boardA[3 * i + 2] \
                and boardA[3 * i] != 0:
            return True, boardA[3 * i]
        if boardA[i] == boardA[3 + i] and boardA[3 + i] == boardA[6 + i] and boardA[i] != 0:
            return True, boardA[i]
    if boardA[0] == boardA[4] and boardA[4] == boardA[8] and boardA[0] != 0:
        return True, boardA[0]
    if boardA[2] == boardA[4] and boardA[4] == boardA[6] and boardA[2] != 0:
        return True, boardA[2]
    for i in range(9):
        if boardA[i] == 0:
            return False, 0
    return True, 0


def switch_turn(boardA):
    one_count = two_count = 0

    for x in boardA:
        if x == 1:
            one_count += 1
        elif x == 2:
            two_count += 1
    if one_count > two_count:
        turn = 2
    else:
        turn = 1

    return turn


def predict(boardA, action):
    next_boardA = copy.copy(boardA)
    turn = switch_turn(boardA)

    next_boardA[action] = turn
    done, winner = end_check(next_boardA)

    reward = 0
    if done and winner == 1: reward = 1
    if done and winner == 2: reward = -1
    if done and winner == 0: reward = 0

    return next_boardA, reward


def convert(boardA):
    string = str()
    for x in boardA:
        string += str(x)
    return string


env = Environment()
agent = Policy_iteration_player(restore=False)
agent_base = policyIterationPlayerBase()
episode = 100
gamma = 0.9

def policy_evaluation(agent):
    
    while True:
        delta = 0.0
        boardA_list = itertools.product([0, 1, 2], repeat=9)
        
        for boardA in boardA_list:
            boardA = list(boardA)
            done, winner = end_check(boardA)
            if not done:
                v = agent.vtable(boardA)

                action = agent.selectAction(boardA)
                next_boardA, reward = predict(boardA, action)
                agent.learnVtable(boardA, reward + gamma * agent.vtable(next_boardA))

                delta = max([delta, abs(v - agent.vtable(boardA))])

        if delta < 0.000001:
            break


def polcyImprovement(agent):
    policyStable = True
    boardA_list = itertools.product([0, 1, 2], repeat=9)
    
    for boardA in boardA_list:
        boardA = list(boardA)
        done, winner = end_check(boardA)
        if not done:
            available_action = get_action(boardA)
            turn = switch_turn(boardA)

            old_action = agent.selectAction(boardA)

            max_value = -9999999
            min_value = 9999999
            
            if turn == 1:
                for action in available_action:
                    next_boardA, reward = predict(boardA, action)
                    vtable = reward + gamma * agent.vtable(next_boardA)
                    if vtable > max_value:
                        max_value = vtable
                        temp_action = action
            else:
                for action in available_action:
                    next_boardA, reward = predict(boardA, action)
                    vtable = reward + gamma * agent.vtable(next_boardA)
                    if vtable < min_value:
                        min_value = vtable
                        temp_action = action

            agent.learnPolicy(boardA, temp_action)

            if old_action != temp_action:
                policyStable = False

    if policyStable:
        return True
    else:
        return False

iteration = 0

#정책반복
while True:
    iteration += 1

    policy_evaluation(agent)
    stop = polcyImprovement(agent)

    win = lose = draw = 0
    count = 0
    for i in range(episode):
        done = 0
        env.reset_board()
        boardA = copy.copy(env.boardA)

        winner = 0
        j = 0
        while not done:
            j += 1
            turn = copy.copy(env.turn)
            if (i + j) % 2 == 1:
                action = agent.selectAction(boardA)
                count += 1
            else:
                action = agent_base.selectAction(boardA, turn)
            next_boardA, done, reward, winner = env.move(action)
            boardA = copy.copy(next_boardA)

        if winner == 0:
            draw += 1
        elif (i + j) % 2 == 1:
            win += 1
        else:
            lose += 1
                
    print("[Iteration %d] Win : %d /  Draw : %d  / Lose : %d" % (iteration, win, draw, lose))
    agent.dataSave()
    if stop:
        break

p1 = Human_player()
p2 = Policy_iteration_player(restore=True)
print("pl player : {}".format(p1.name))
print("p2 player : {}".format(p2.name))


auto = False
games = 100    
p1_score = 0
p2_score = 0
draw_score = 0
env = Environment()
env.reset_board()
boardA = copy.copy(env.boardA)

if auto: 
    for j in tqdm(range(games)):
        
        np.random.seed(j)
        env = Environment()
        
        for i in range(10000):
            if ((-1)**i) == 1:
                action = p1.selectAction(boardA)
            else:
                action = p2.selectAction(boardA)
                
            next_boardA, done, reward, winner = env.move(action)
            boardA = copy.copy(next_boardA)
            env.printBoard()
            
            if done == True:        
                if reward == 1:
                    print("winner is p1({})".format(p1.name))
                    p1_score += 1
                elif reward == -1:
                    print("winner is p2({})".format(p2.name))
                    p2_score += 1
                else:
                    print("draw")
                    draw_score += 1
                break
                
        done = 0
        env.reset_board()
        winner = 0
        boardA = copy.copy(env.boardA)

else:                
    np.random.seed(1)
    while True:
        env = Environment()
        env.print = False
        for i in range(10000):
            if ((-1)**i) == 1:
                action = p1.selectAction(boardA)
            else:
                action = p2.selectAction(boardA)  
            next_boardA, done, reward, winner = env.move(action)
            boardA = copy.copy(next_boardA)
            env.printBoard()
                
            if done == True:
                if reward == 1:
                    print("winner is p1({})".format(p1.name))
                    p1_score += 1
                elif reward == -1:
                    print("winner is p2({})".format(p2.name))
                    p2_score += 1
                else:
                    print("draw")
                    draw_score += 1
                break
               
        print("final result")
        env.printBoard()
 
        answer = input("More Game? (y/n)")

        if answer == 'n':
            break
        else:
            done = 0
            env.reset_board()
            winner = 0
            boardA = copy.copy(env.boardA)

print("p1({}) = {} p2({}) = {} draw = {}".format(p1.name, p1_score,p2.name, p2_score,draw_score))
