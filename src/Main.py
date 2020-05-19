"""
------------------------------------------------------------------------
[Main Driver]
------------------------------------------------------------------------
Author: Kaish
File Name: Main.py
Version: 2020-03-01
------------------------------------------------------------------------
"""

# Import

from Basic_Calculation import basic_cal_main
from Basic_Func import *
from Differentiation import diff_main
from Integration import int_main


# Execute

intro()
print("="*120)

instruction()

menu()

main_menu_select = 'NULL'

while main_menu_select != '0':
    main_menu_select = input("~~~> Select Menu Item (1: to display menu): ")
    
    if main_menu_select == '0':
        print("\n:::> End")
        
    elif main_menu_select == '1':
        menu()
        
    elif main_menu_select == '2':
        basic_cal_main()
        
    elif main_menu_select == '3':
        diff_main()
        
    elif main_menu_select == '4':
        int_main()
        
    elif main_menu_select == '5':
        print("Path not yet coded")
    
    else:
        print("Invalid Input, try again")

print()
print("="*120)
outro()