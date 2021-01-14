from sympy import * 
  
M = Matrix([[1, 0, 1, 3], [2, 3, 4, 7], [-1, -3, -3, -4]]) 

M_rref = M.rref()   
      
print(M_rref)