"""
------------------------------------------------------------------------
[Basic Calculation Functions]
------------------------------------------------------------------------
Author: Kaish
File Name: Basic_Calculation.py
Version: 2020-03-02
------------------------------------------------------------------------
"""

# Import

from CAS import linear_CAS, sol_quadratic_CAS


# Basic Calculation Menu
def basic_cal_menu():
    """
    -------------------------------------------------------
    Prints the Differentiation Menu
    Use: basic_cal_menu()
    -------------------------------------------------------
    Parameters:
       NONE
    Returns:
       NONE
    ------------------------------------------------------
    """
    
    print("""
    Basic Calculation Menu
    ----------------------
    0) Return to Main Menu
    1) Algebraic Simplification
    2) Basic Math
    3) Solve Quadratic Equation
    """)
    
    
# Basic Calculation Main Program

def basic_cal_main():
    """
    -------------------------------------------------------
    Basic Calculation Functions - Main Driver
    Use: basic_cal_main()
    -------------------------------------------------------
    Parameters:
       NONE
    Returns:
       NONE
    ------------------------------------------------------
    """
    
    basic_cal_menu()
    basic_cal_select = 'NULL'

    while basic_cal_select != '0':
        basic_cal_select = input("~~> Select a method (0: return to main menu): ")
    
        if basic_cal_select == '0':
            print("\n:::> Return\n")
        
        elif basic_cal_select == '1':
            print("\nAlgebraic Simplification\n------------------------")
            func = input("\~~> Enter string to evaluate: ")
            result = linear_CAS(func)
            print("\n\t==> Result: x = {:.2f}\n".format(result))
        
        elif basic_cal_select == '2':
            print("\nBasic Math Evaluation\n---------------------")
            func = input("\~~> Enter string to evaluate: ")
            result = basic_eval(func)
            print("\n\t==> Result: {:.2f}\n".format(result))
            
        elif basic_cal_select == '3':
            print("\nSolve Quadratic Equation\n------------------------")
            func = input("\~~> Enter string to evaluate: ")
            root_1, root_2 = sol_quadratic_CAS(func)
            print("\n\t==> Result: Root_1 = {}, Root_2 = {}\n".format(root_1,root_2))
        
        else:
            print("Invalid Input, try again")
        
    print()
    
    
    
def basic_eval(func):
    """
    -------------------------------------------------------
    Evaluates a given math string at and returns the result
    Use: result = basic_eval(func)
    -------------------------------------------------------
    Parameters:
       func - string of function to be evaluated (str)
    Returns:
       result - end result calculated (float) 
    ------------------------------------------------------
    """
    
    # Using the Built-In Python Eval Function
    result = eval(func)
    
    return result