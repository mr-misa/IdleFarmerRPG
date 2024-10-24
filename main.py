#standard imports
import cmd
import textwrap
import sys
import os
import time
import random

# game functionality imports
import game
import game_data_handler

#call the load game data to check if the file exists if it does this function call makes sure the file is created with initial data.
game_data_handler.load_game()

#start the game
game.start_game()