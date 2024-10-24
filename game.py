#standrd imports
import cmd
import textwrap
import sys
import os
import time
import random

# game functionality imports
import actions_menu

### End Of Imports ###

### Functions ###
# Function help is used to display the help section. #
def help():
    print("The game will show help.")

# Function used to quit the game #
def quit():
    print("The game will quit.")
    exit()

# Function to display the main menu. #
def display_main_menu():
    print("#"*21)
    game_title = " Idle Farmer RPG "
    print(f"{game_title:^21}")
    print(f"{'Main Menu':^21}")
    menu_options = ["1. Play", "2. Help", "3. Quit"]
    for option in menu_options:
        print(f"{option:^21}")
    print("#"*21)
### End Of Functions ###

### Main Entry Point ###
def start_game():
    #clear the screen and display the main menu
    os.system( "cls" if os.name == 'nt' else "clear")
    display_main_menu()

    while True:
        #wait for user to make a menu choice
        menu_choice = int(input("> "))

        if menu_choice == 1:
            #call the play function from actions menu
            actions_menu.play()
            os.system( "cls" if os.name == 'nt' else "clear")
            
            #once flow returns back to this file display the main meni again
            display_main_menu()
        elif menu_choice == 2:
            #options 2 = help menu
            help()

        elif menu_choice == 3:
            #option 3 = quit
            quit()
            break
        else: 
            print("Please select a valid option.")
    ### End Of Main Entry Point ###


#function for pausing the game to wait for user input 
#useful for displayinh information to the user - to bringattention to the user
def pause():
    #pause message
    print("Press any key to continue...", end='', flush=True)

    if os.name == 'nt':  
        # For Windows
        import msvcrt
        msvcrt.getch()
    else:  
        # For Unix-like systems (Linux, macOS)
        import termios
        import tty

        # Set terminal to raw mode
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            sys.stdin.read(1)  # Wait for a single key press
        finally:
            # Restore terminal settings
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    print()  # Move to the next line after the key press
