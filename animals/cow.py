#standard imports
import cmd
import textwrap
import sys
import os
import time
import random

# game functionality imports
import stats
import game_data_handler


#show all stats for the cows, all stats stored in save_game1.json
def display_cow_stats():

    #get the save game data from the json file
    game_data = game_data_handler.load_game()
    
    #get the cow data from the game data
    cow_data = game_data["animals"]["cows"]

    #define the menu attributes and display the cow stats nicely
    menu_width = 25
    print("#"*25)
    print(f"#{'Cows: '+str(cow_data['num_cows_owned']):^{menu_width-2}}#")
    print(f"#{'Corrals: '+str(cow_data['num_cow_corrals']):^{menu_width-2}}#")
    print(f"#{'Liters: '+str(cow_data['liters_of_milk']):^{menu_width-2}}#")
    print("#"*25)

#menu to display all cow actions
# the input parameter is ti determine if the menu needs to be cleared or not
def display_cow_actions(clear_menu):
    #array of cow actions available
    cow_actions = ["1. Collect Milk", "2. Back To Animals Menu"]

    #check if menu needs to be cleared
    if clear_menu:
        os.system( "cls" if os.name == 'nt' else "clear")
    
    display_cow_stats()

    #display the available cow actions nicely
    print("Available Actions")
    for action in cow_actions:
        print(f"{action:<50}")


#action function to collect milk from the cows
def collect_milk():

    #display a message and pause the game for a bit to add an affect
    print("... collecting milk ...")
    sleep_secs = 3
    time.sleep(sleep_secs)

    #generate a random amount of liters of milk
    random_amount_of_liters = random.randint(0,2)

    #display number of liters gathered
    print("... collected: "+str(random_amount_of_liters)+" liters\n")
    
    #add the randomly generated liters of milk to the stats.py file
    stats.cow_milk_liters_count += random_amount_of_liters

    #grab the game data
    game_data = game_data_handler.load_game()

    #add the randomly amount of generated liters of milk to the save game file
    game_data["animals"]["cows"]["liters_of_milk"] += random_amount_of_liters

    #save the game data after adding the liters of milk
    game_data_handler.save_game(game_data)

# this function is called from animals_menu.py to allow user to select an available action for the cows
def cow_menu():
    display_cow_actions(clear_menu=True)

    while True:
        #wait for user input to perform a cow action
        menu_option = int(input("> "))
        
        if menu_option == 1:
            os.system( "cls" if os.name == 'nt' else "clear")
            
            #option 1 = milk cows
            collect_milk()
            display_cow_actions(clear_menu=False)

        elif menu_option == 2:
            #option 2 is the back option to previous menu
            break
        else:
            print("enter valid option")

