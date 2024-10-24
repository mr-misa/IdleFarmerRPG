#standard imporst
import json
import os

#function to save the game data
def save_game(data, path="save_game1.json"):
    
    save_game_file_path = path
    
    try:
        with open(save_game_file_path, 'r') as save_file:
            #load the json save game file
            save_game_data = json.load(save_file)
            
        for key, value in data.items():
            save_game_data[key] = value
            
        with open(save_game_file_path, 'w') as save_file:
            #save the json save game file with the data that was passed in
            json.dump(save_game_data, save_file, indent=4)
        
        #print("saved to json")
            
    #handle exceptions below
    except FileNotFoundError:
        print("The file was not found.")
    
    except json.JSONDecodeError:
        print("Error decoding JSON. Check if the file is valid JSON.")
    
    except Exception as e:
        print(f"An error has occurred: {e}")


#function to load game data
def load_game(path="save_game1.json"):
    try:
        file_name = path
        
        #check if the file exists
        if os.path.exists(file_name):
            #file will be opened and worked with not created
            #print("file will be opened and worked with not created")
            
            with open(file_name, 'r+') as save_game_file:
                #if the file exists load the json and return it
                save_game_data = json.load(save_game_file)
                return save_game_data
            
        else:
            #if the file does not exist the file will be created instead
            #print("file was created")
            with open(file_name, 'w') as save_game_file:
                #create the file with initial data
                initial_data = {
                    "name": "Player 1",
                    "money": 5000,
                    "animals": {
                        "cows": {
                            "liters_of_milk": 0.0,
                            "num_cows_owned": 1,
                            "num_cow_corrals":0
                        },
                        "chickens": {
                            "num_chicken_eggs": 0,
                            "num_chickens_owned": 3,
                            "num_chicken_coops":0
                        }
                    },
                    "fields": [
                        {
                            "id": 1,
                            "crop_type": "corn",
                            "growth_stage": 3,
                            "needs_fertilizer": True,
                            "needs_watering": False
                        },
                        {
                            "id": 2,
                            "crop_type": "wheat",
                            "growth_stage": 1,
                            "needs_fertilizer": False,
                            "needs_watering": False
                        },
                        {
                            "id": 3,
                            "crop_type": "soy",
                            "growth_stage": 2,
                            "needs_fertilizer": True,
                            "needs_watering": True
                        }
                    ]
                }
                
                #save the initial data to json
                json.dump(initial_data, save_game_file, indent=4)
                
                
            with open(file_name, 'r+') as save_game_file:
                #load json data after saving initial data and return the data
                save_game_data = json.load(save_game_file)
                return save_game_data
        
    #handle exceptions below
    except FileNotFoundError:
        print("The file was not found.")
        
    except json.JSONDecodeError:
        print("Error decoding JSON. Check if the file is valid JSON.")
        
    except Exception as e:
        print(f"An error has occurred: {e}")
