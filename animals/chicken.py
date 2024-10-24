#standard imports
import cmd
import textwrap
import sys
import os
import time
import random

#game functionality imports
import stats
import game_data_handler


#Function used to display all the stats for the chickens all stats stored in save_game1.json
def display_chicken_stats():
    #get the game dta
    game_data = game_data_handler.load_game()
    
    #get the chicken data from the game dta
    chicken_data = game_data["animals"]["chickens"]

    #define menu attributes and display the chicken stats nicely
    menu_width = 25
    print("#"*25)
    print(f"#{'Chickens: '+str(chicken_data['num_chickens_owned']):^{menu_width-2}}#")
    print(f"#{'Coops: '+str(chicken_data['num_chicken_coops']):^{menu_width-2}}#")
    print(f"#{'Eggs: '+str(chicken_data['num_chicken_eggs']):^{menu_width-2}}#")
    print("#"*25)

#display all available chicken actions
# the clear_menu flag is used to determin if the menu needs to be cleared or not
def display_chicken_actions(clear_menu):
    chicken_actions = ["1. Collect Eggs", "2. Back To Animals Menu"]

    #check if the screen needs to be cleared
    if clear_menu:
        os.system( "cls" if os.name == 'nt' else "clear")
    
    display_chicken_stats()

    #display all available chicken actions nicely
    print("Available Actions")
    for action in chicken_actions:
        print(f"{action:<50}")


# this function is an action for chickens to collect all the eggs
def collect_eggs():
    print("... collecting eggs ...")
    
    #pause the game for a bit to add an affect
    sleep_secs = 3
    time.sleep(sleep_secs)

    #generate a random number of eggs
    random_amount_of_eggs = random.randint(0,2)

    #display how many eggs were collected
    print("... collected: "+str(random_amount_of_eggs)+" eggs\n")
    
    #add the randon generate amount of eggs to the egg count in the stats.py file
    stats.chicken_egg_count += random_amount_of_eggs

    #load the game game data
    game_data = game_data_handler.load_game()

    #grab the current number of eggs from the save game data and add the number of randomly generated eggs
    game_data["animals"]["chickens"]["num_chicken_eggs"] += random_amount_of_eggs
    
    #save the game data after adding the random number of eggs
    game_data_handler.save_game(game_data)


#function display the menu and wait for user to perform an action
def chicken_menu():
    
    #display the chicken actions
    display_chicken_actions(clear_menu=True)

    while True:
        #wait for user input to take chicken action
        menu_option = int(input("> "))
        
        if menu_option == 1:
            os.system( "cls" if os.name == 'nt' else "clear")
            
            #option 1 = collect eggs action
            collect_eggs()
            display_chicken_actions(clear_menu=False)

        elif menu_option == 2:
            #return to the previous menu
            break
        else:
            print("enter valid option")

