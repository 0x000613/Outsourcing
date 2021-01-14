class Patient:
    def __init__(self, num, day_diagnosed, age, sex_gender, postal, state, temps, days_symptomatic):
        # num = int num
        self.num = int(num)
        
        # day_diagnosed = int day_diagnosed
        self.day_diagnosed = int(day_diagnosed)
        
        # age = int age
        self.age = int(age)
        
        # sex_gender
        sex_gender = sex_gender.upper()
        BOY = ['BOY', 'MAN', 'MALE', 'HOMME']
        GIRL = ['GIRL', 'WOMMAN', 'FEMALE', 'FEMME']
        if sex_gender in BOY: self.sex_gender = 'M'
        elif sex_gender in GIRL: self.sex_gender = 'F'
        else: self.sex_gender = 'X'
        
        # postal
        self.postal = postal[0:3]
        if postal[0] != 'H' or postal[1].isdigit() != True or postal[2].isalpha() != True: self.postal = "000"
        
        # state
        self.state = state

        # temps
        self.temps = float(temps.replace(',', '.'))
        if self.temps == None or self.temps.isdigit() != False: self.temps = 0
        elif self.temps > 45: self.temps = round((self.temps - 32) * 5/9, 2)

        # days_symptomatic
        self.days_symptomatic = int(days_symptomatic)
    
    def __str__(self):
        patients = [str(self.num), str(self.age), self.sex_gender,
                    self.postal, str(self.day_diagnosed), self.state,
                    str(self.days_symptomatic), str(self.temps)]
        
        if len(self.temps) > 1:
            ';'.join(self.temps)
         
        
        return '\t'.join(patients)
        
    def update(self, p1):
        if self.num == p1.num and self.sex_gender == p1.sex_gender and self.postal == p1.postal: 
            self.days_symptomatic = p1.days_symptomatic
            self.state = p1.state
            self.temps.append(p1.temps)
        else:
            raise AssertionError ("num / sex_gender / postal are not the same")