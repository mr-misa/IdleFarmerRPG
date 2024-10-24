#standard imports
import cmd
import textwrap
import sys
import os
import time
import random

#game functionality imports
import game
import game_data_handler

#function to display all fields in a nice table
def display_fields_in_table ():

    #clear the screen when displaying the table to make it looks nice
    os.system( "cls" if os.name == 'nt' else "clear")

    #get game data from the save file
    game_data  = game_data_handler.load_game()

    #get the array of fields from the save game file
    fields = game_data["fields"]

    #the next few lines handle printing out the table
    #define table headers and print out hte header
    print("-"*75)
    id_column= "ID"
    crop_column = "Crop Type"
    needs_watering_column = "Needs Water"
    needs_fertilizer_column = "Needs Fertilizer"
    growth_stage_column = "Growth Stage"
    
    table_header = f"{id_column:^6} | {growth_stage_column:^14} | {crop_column:^11} | {needs_watering_column:^13} | {needs_fertilizer_column:^17}"
    print(table_header)
    print("-"*75)
    
    #array to temporarily store field info for displaying
    field_information = []
    
    #process each field in the array
    for field in fields:
        #grab each attribute for each field
        id = str(field['id'])
        crop = str(field['crop_type'])
        needs_water = field['needs_watering']
        needs_fertilizer = field['needs_fertilizer']
        growth_stage = field ['growth_stage']
        
        #check if the field needs to be watered
        water = ""
        if needs_water:
            water = "Yes"
        else:
            water = "No"
        
        #check if the field needs to be fertilized
        fertilize = ""
        if needs_fertilizer:
            fertilize = "Yes"
        else: 
            fertilize = "No"
        
        #temporarily create a string to store field info nicely and display it nicely
        tempstring = f"{id:^6} | {growth_stage:^14} | {crop:^11} | {water:^13} | {fertilize:^17}"
        
        #append each temp string to the field info array
        field_information.append(tempstring)
        
    #process each string in the below loop
    for item in field_information:
        print(item)
        
    print("-"*75)


#function to process the details of a field to check what actions can be taken on it
def get_field_actions(field_details):

    #grab the attribues for the field in question
    growth_stage = field_details["growth_stage"]
    is_fertilized = field_details["needs_fertilizer"]
    needs_watering = field_details["needs_watering"]

    #array to store the available actions
    actions = []

    #if the growth stage is 3 then we can perform the harvest action
    #if growth stage is zero 0 then field can be sowed on 
    if growth_stage == 3:
        actions.append("Harvest")
    
    #check if field can be fertilized
    if is_fertilized:
        actions.append("Fertilize")

    #check if field can be watered
    if needs_watering:
        actions.append("Water")
    
    #always add the back option
    actions.append("Back")
    
    return actions


#function to get details about a field by its ID
def get_field_details_by_id(field_id):
    
    #clear the screen to make it looks nice
    os.system( "cls" if os.name == 'nt' else "clear")
    
    #offset the field_id by 1 for proper array indexing
    field_id = int(field_id) - 1

    #get the game data from the save game file
    game_data = game_data_handler.load_game()

    #get all the fields array from the game daya
    fields = game_data["fields"]
    
    if 0 <= field_id < len(fields):
        #if the field_id is within the array bounds then we can get the field by its ID
        field = fields[field_id]
    
        #the next few lines are to display the table of field details
        table_header = f"{'ID':^6} | {'Growth Stage':^14} | {'Crop Type':^11} | {'Needs Water':^13} | {'Needs Fertilizer':^17}"
        print("-"*75)
        print(table_header)
        print("-"*75)
        
        #get the fields attributes
        id = field['id']
        crop = field['crop_type']
        needs_water = field['needs_watering']
        needs_fertilizer = field['needs_fertilizer']
        growth_stage = field['growth_stage']
        
        #check if a field needs watering
        water = ""
        if needs_water:
            water = "Yes"
        else:
            water = "No"

        #check if a field can be fertilized
        fertilize = ""
        if needs_fertilizer:
            fertilize = "Yes"
        else:
            fertilize = "No"
            
        #print out the field details 
        print(f"{id:^6} | {growth_stage:^14} | {crop:^11} | {water:^13} | {fertilize:^17}")
        
        print("-"*75)

        #display all the available actions for the field in question
        print("Available Actions:")

        #get the field chores vis the get get_field_actions function
        field_chores = get_field_actions(field)
        
        #use the following for loop to display all the actions
        count = 0
        for chore in field_chores:
            count += 1
            print(f"{count}. {chore:<50}")

        print("-"*25)

        while True:
            #while true keep asking for user input to perform an action onthe field
            chore_action = int(input("> "))

            if len(field_chores) == 1:
                #if the array of actions only has 1 actions 
                if chore_action == 1:
                    #if chore actions is 1 and array size was 1 this means that the only option is 1. Back so we break
                    break
                else:
                    print("Invalid Choice")
            else:
                #else if the array has more than 1 actions
                if chore_action == len(field_chores):
                    #if the user enters a value that is the same size as the array of actions this means the user selected the back option which is always the last option
                    break
                else:
                    #any other value that is not the size of array then:
                    chore_action = int(chore_action)-1

                    if 0 <= chore_action < len(field_chores):
                        #as long as the action is within range
                        #get the string value for the chosen action
                        #we use string reperesentations because it works for dynamic menus since the menu will not always be teh same
                        
                        chore_selection = field_chores[chore_action]

                        if chore_selection == "Harvest":
                            #harves action
                            print("Harvesting")
                        elif chore_selection == "Fertilize":
                            #fertilize action
                            print("Fertilizing")
                        elif chore_selection == "Water":
                            #water action
                            print("Watering")
                    else:
                        print("Invalid Choice")
    else:
        print(f"You do not own the field with ID: {field_id}.")
        


#this function is called form the actions menu when user selects to Go To Fields
def show_fields():

    while True:
        #display the fields in a table
        display_fields_in_table()

        #ask the user for input to what filed they want to interact with
        print("Which Field Would You Like To Interact With?")
        print("enter 'x' to exit")
        field_id = input("> ")

        if field_id == 'x' or field_id == 'X':
            #if the user input is x or X then we exit from the fields and go back to the previous menus
            break
        else:
            #get the game data and check for the amount of total fields
            game_data = game_data_handler.load_game()
            fields = game_data["fields"]
            total_fields = len(fields)

            field_id = int(field_id)
            field_id_minus_1 = field_id -1
    
            if 0 <= field_id_minus_1 < total_fields:
                #if the field is within range then we get field by ID
                get_field_details_by_id(field_id)
            else:
                #let the user know they cannot interact with that field
                os.system( "cls" if os.name == 'nt' else "clear")
                print(f"You do not own the field with ID: {field_id}.")
                game.pause()
