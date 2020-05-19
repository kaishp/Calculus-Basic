"""
------------------------------------------------------------------------
[Differentiation Functions]
------------------------------------------------------------------------
Author: Kaish
File Name: Differentiation.py
Version: 2020-03-01
------------------------------------------------------------------------
"""

# Constants

H = 0.00000001


# Differentiation Menu

def diff_menu():
    """
    -------------------------------------------------------
    Prints the Differentiation Menu
    Use: diff_menu()
    -------------------------------------------------------
    Parameters:
       NONE
    Returns:
       NONE
    ------------------------------------------------------
    """
    
    print("""
    Differentiation Menu
    --------------------
    0) Return to Main Menu
    1) Function Differentiation
    2) Particular Solution
    """)
    
    
# Differentiation Main Program

def diff_main():
    """
    -------------------------------------------------------
    Differentiation Functions - Main Driver
    Use: diff_main()
    -------------------------------------------------------
    Parameters:
       NONE
    Returns:
       NONE
    ------------------------------------------------------
    """
    
    diff_menu()
    diff_menu_select = 'NULL'

    while diff_menu_select != '0':
        diff_menu_select = input("~~> Select a method (0: return to main menu): ")
    
        if diff_menu_select == '0':
            print("\n:::> Return\n")
        
        elif diff_menu_select == '1':
            print("Path not yet coded\n")
        
        elif diff_menu_select == '2':
            print("\nParticular Solution Evaluation\n------------------------------")
            func = input("~~> Enter Function to evaluate:  ")
            x = float(input("~~> Enter point of evaluation: "))
            result = f_prime_eval(x, func)
            print("\n\t==> Result: {:.2f}\n".format(result))
        
        else:
            print("Invalid Input, try again")
        
    print()
    
    
def f(x, func):
    """
    -------------------------------------------------------
    Function
    Use: a = f(x)
    -------------------------------------------------------
    Parameters:
        x - point of evaluation (float)
        func - string of function to be evaluated (str)
    Returns:
        result - evaluated function at point x (float)
    ------------------------------------------------------
    """
    
    return eval(func)
    
    
    
def f_prime(x):
    """
    -------------------------------------------------------
    Differentiates a given function
    Use: a = f_prime(x)
    -------------------------------------------------------
    Parameters:
       x - point of evaluation (float)
    Returns:
       NONE
    ------------------------------------------------------
    """
    a = x
    
    return a


def f_prime_eval(x, func):
    """
    -------------------------------------------------------
    Differentiates and evaluates a given function (x) at 
    point (n)
    Use: a = f_prime_eval(x,n)
    -------------------------------------------------------
    Parameters:
       x - point of evaluation (float)
       func - string of function to be evaluated (str)
    Returns:
       result - end result calculated (float) 
    ------------------------------------------------------
    """
    top = f(x + H, func) - f(x, func)
    bottom = H
    result = top / bottom
    
    return result
    