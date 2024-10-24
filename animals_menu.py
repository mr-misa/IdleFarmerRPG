#standard imports
import cmd
import textwrap
import sys
import os
import time
import random

#import all the animals
from animals import chicken
from animals import cow

#Function used to display all available animals to interact with
def display_animals():
    #display the available aniams to interact with nicely
    os.system( "cls" if os.name == 'nt' else "clear")
    animals = ["1. Cows", "2. Chickens","3. Back To Actions Menu"]
    print(f"{'Animals':<50}")
    for animal in animals: 
        print(f"{animal:<50}")

#the function is called from actions_menu.py in order to display all the animals and wait for user to select one to interact with
def choose_animal():
    #clear the screen and display the animals
    os.system( "cls" if os.name == 'nt' else "clear")
    display_animals()

    while True:
        #wait for user input
        animal_option = int(input("> "))

        if animal_option == 1:
            #option 1 = cows when this option is select it will display all availalbe cow options
            cow.cow_menu()

            #when flow returns back to this file display all animals again
            display_animals()

        elif animal_option == 2:

            #option 2 = chickens when this option is selected display all available chicken actions
            chicken.chicken_menu()

            #when flow returns back to this file display all animals again
            display_animals()

        elif animal_option == 3:
            #this option is to return to the previous menu
            break
        else:
            print("enter a valid option")

