import json     #it needed to convert python lists and dictionaries into a text and vice versa
import os        #it verify if workout file is on my computer
from datetime import datetime, timedelta   # to auto_capture log out sessions

FILE_NAME = "workouts.txt"

def load_sessions():
    """
    Reads workouts.txt and returns the list of saved sessions.
    If the file doesn't exist yet, it returns an empty list.
    Each session is a dictionary with a date and a list of exercises.
    """
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        content = file.read().strip()
 return []

    sessions = json.loads(content)
    return sessions

def check_personal_best(sessions, new_sessions):
    """
    compare each  exercise in new_sessions against  all historical sessions and print a message if a new personal best volume 
    is achieved.
    """
  for exercise in new_sessions["exercises"]
      exercise_name = exercise["name"]
      current_weight = calculate_volume(exercise)
    # Cpllect historical volume for the same exercise name 
historical_volume = [] 




