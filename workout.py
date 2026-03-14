# workout.py
# Project 9 - Workout Tracker
# Tech4Girls Backend Cohort 4


import json     #it needed to convert python lists and dictionaries into a text and vice versa
from datetime import datetime, timedelta   # to auto_capture log out sessions

FILE_NAME = "workouts.txt"
class WorkoutSession:

    def __init__(self, date, exercises):       # The date the workout happened
        self.date = date                       # A list of exercises done in this session
        self.exercises = exercises

    def get_total_volume(self):                 # Add up the volume of every exercise in this session
        total = 0
        for exercise in self.exercises:
            total = total + exercise["volume"]
        return total

    def to_dictionary(self):                   # Convert this session into a dictionary so we can save it to a file
        return {
            "date": self.date,
            "exercises": self.exercises,
           "total_volume": self.get_total_volume()
        }
    def load_sessions():                         # Try to open the file and read the saved sessions
        try:                                        # If the file does not exist yet, just return an empty list
        file = open(FILE_NAME, "r")
        content = file.read().strip()
        file.close()                             # If the file is empty, return an empty list   

        if content == "":
            return []

    sessions = json.loads(content)            # Convert the text back into a Python list
        return sessions

    except FileNotFoundError:
        return []
    
    def save_sessions(sessions):
    
       file = open(FILE_NAME, "w")
       json.dump(sessions, file, indent=2)
       file.close()
      print("Sessions saved to workouts.txt")

     
# VOLUME CALCULATION
# volume = sets x reps x weight

def calculate_volume(sets, reps, weight):

    if weight >= 1:
    volume = sets * reps * weight
    return volume


