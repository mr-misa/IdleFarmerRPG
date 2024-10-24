#standard imports
import cmd
import textwrap
import sys
import os
import time
import random

#game functionality imports
import animals_menu
import fields


#menu to display the the actions menu
def display_actions_menu():

    #clear the screen and display the menu nicely
    os.system( "cls" if os.name == 'nt' else "clear")
    print(f"{'Actions Menu':<50}")
    actions = ["1. Go To Fields", "2. Go To Animals", "3. Main Menu"]
    for action in actions:
        print(f"{action:<50}")

#play function is called from game.py when user selects to play the game
def play():
    
    # show the actions menu 
    display_actions_menu()
    while True:
        
        #wait for user to select a menu action
        action_option = int(input("> "))

        # go to fields option
        if action_option == 1:
            #show the fields menu 
            fields.show_fields()

            #after the flow returns to this function it display the actions menu
            display_actions_menu()
        
        #go to animals option
        elif action_option == 2:

            #display the animals menu from animals_menu.py
            animals_menu.choose_animal()

            #when flow returns back to this function display the actions menu again
            display_actions_menu()
        elif action_option == 3:
            #action to go back to main menu
            break
        else:
            print("enter a valid option.")

