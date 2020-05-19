"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Kaish
File Name: Integration.py
Version: 2020-03-01
------------------------------------------------------------------------
"""

# Constants

N = 1000000


# Integration Menu

def int_menu():
    """
    -------------------------------------------------------
    Prints the Integration Menu
    Use: int_menu()
    -------------------------------------------------------
    Parameters:
       NONE
    Returns:
       NONE
    ------------------------------------------------------
    """
    
    print("""
    Integration Menu
    ----------------
    0) Return to Main Menu
    1) Indefinite
    2) Definite
    """)
    
    
# Integration Main Program

def int_main():
    """
    -------------------------------------------------------
    Integration Functions - Main Driver
    Use: int_main()
    -------------------------------------------------------
    Parameters:
       NONE
    Returns:
       NONE
    ------------------------------------------------------
    """
    
    int_menu()
    int_menu_select = 'NULL'

    while int_menu_select != '0':
        int_menu_select = input("~~> Select a method (0: return to main menu): ")
    
        if int_menu_select == '0':
            print("\n:::> Return\n")
        
        elif int_menu_select == '1':
            print("Path not yet coded\n")
        
        elif int_menu_select == '2':
            print("\nDefinite Integral\n----------------")
            print("""
              b
             ┌┐
             |   f(x) * dx
            └┘
            a
            """)
            a = int(input("\~~> Enter lower bound (a): "))
            b = int(input("\~~> Enter upper bound (b): "))
            func = input("\~~> Enter string to evaluate: ")
            sum = def_int_eval(a, b, func)
            print("\n\t==> Result: {:.2f}\n".format(sum))
        
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


def def_int_eval(a, b, func):
    """
    -------------------------------------------------------
    Evaluates the definite integral at given bounds
    Use: sum = def_int_eval(a, b, func)
    -------------------------------------------------------
    Parameters:
       a - lower bound of definite integral (float)
       b - upper bound of definite integral (float)
       func - string of function to be evaluated (str)
    Returns:
       sum - end result calculated (float) 
    ------------------------------------------------------
    """
    if a > b:
        a, b = b, a

    dx = (b - a) / N
    sum = 0.0
    f_i = 0.0

    for i in range(N):
        x_i = a + dx * i
        f_i = f(x_i, func)
        sum += f_i * dx
    
    return sum