"""
------------------------------------------------------------------------
[Computer Algebraic System]
------------------------------------------------------------------------
Author: Kaish
File Name: CAS.py
Version: 2020-04-30
------------------------------------------------------------------------
"""

# Import


# Functions

def linear_CAS(equ):
    """
    -------------------------------------------------------
    Evaluates a given linear algebraic string returns the 
    result
    Use: result = linear_CAS(equ)
    -------------------------------------------------------
    Parameters:
       equ - string of function to be evaluated (str)
    Returns:
       result - end result calculated (float) 
    ------------------------------------------------------
    """
    equ = equ.replace(" ", "") # Trimming the Equation (Removing all spaces)
    n = len(equ) # Finding length of Equation
    sign = 1
    coefficient = 0
    total = 0
    i = 0
    
    # Traversing the Equation String
    for j in range(0, n):
        
        # When a sign is found
        if (equ[j] == '+' or equ[j] == '-'):
        
            if (j > i):
                total = (total + sign * int(equ[i: j]))
            
            i = j
            
        # In situations like x, -x and +x
        elif (equ[j] == 'x'):
            
            # When +x
            if ((i == j) or equ[j - 1]== '+'):
                coefficient += sign
                
            # When -x
            elif (equ[j - 1] == '-'):
                coefficient -= sign
                
            # When x
            else:
                coefficient = (coefficient + sign * int(equ[i:j]))
                
            i = j + 1
                
                
        # When '=' is reached, move everything to LHS (flip signs)
        elif (equ[j] == '='):
            
            if (j > i):
                total = (total + sign * int(equ[i:j]))
                
            sign = -1
            i = j + 1
            
        
    # Lookout for number at end
    if (i < n):
        total = (total + sign * int(equ[i: n]))
            
    # Infinite Number of Solutions
    if (coefficient == 0 and total == 0):
        return "Infinite Solutions to Equation"
        
    # No Solutions Exists
    if (coefficient == 0 and total):
        return "No Solutions to Equation"
    
    
    # Finding the final Result, here '-' sign added infront of total
    # This is done to move the result to the RHS
    result = -total / coefficient
    
    return result




def sol_quadratic_CAS(func):
    """
    -------------------------------------------------------
    Evaluates a quadratic string and returns the roots
    Use: result = sol_quadratic(func)
    -------------------------------------------------------
    Parameters:
       func - string of function to be evaluated (str)
    Returns:
       root_1 - first root of equation (str) 
       root_2 - second root of equation (str)
    ------------------------------------------------------
    """
    func = func.replace(" ", "") # Trimming the Function (Removing all spaces)
    n = len(func) # Finding length of Function 
    sign = 1
    a = 0
    b = 0
    c = 0
    i = 0
    
    # Traversing the Equation String
    for j in range(0, n):
        
        if (func[j] == 'x'):
            
            if (j + 1 < n):
        
                # Finding value of a
                if (func[j + 1] == '^' and func[j + 2] == '2'):
                    
                    # In situations like x^2, -x^2 and +x^2
                    if (i == j):
                        a = sign * 1
                        i = j
                    
                    # When Coefficient is not 1 or -1 
                    else:
                        a = sign * int(func[i:j])
                        i = j
                
                # Finding value of b
                elif (func[j+1] != '^'):
                    
                    # In situations like x, -x and +x
                    if (i == j):
                        b = sign * 1
                        i = j
                        
                    # When Coefficient is not 1 or -1
                    else:
                        b = sign * int(func[i:j])
                        i = j
            
        # When pointing at '+'
        elif (func[j] == '+'):
            sign = 1
            i = j + 1
           
        # When pointing at '-' 
        elif (func[j] == '-'):
            sign = -1
            i = j + 1
        
        # When pointing at '='
        elif (func[j] == '='):            
            c = c + sign * int(func[i:j])
            sign = -1
            i = j + 1
            
    # Lookout for number at end      
    if (i < n):
        c = c - sign * int(func[i: n])
    
    # Finding value of Delta
    delta = b**2 - 4 * a * c
    
    # Real Solution
    if delta > 0:
        root_1 = "{:.2f}".format((-b**2 + (delta)**(1/2)) / (2 * a))
        root_2 = "{:.2f}".format((-b**2 - (delta)**(1/2)) / (2 * a))
       
    # Unreal Solution 
    elif delta < 0:
        complex = (-delta)**(1/2) / (2 * a)
        real = -b**2 / (2 * a)
        root_1 = "{:.2f} + {:.2f}i".format(real, complex)
        root_2 = "{:.2f} - {:.2f}i".format(real, complex)
    
    return root_1, root_2