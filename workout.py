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
            file.close()  

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

def log_session(sessions):
    print("\n====== LOG NEW SESSION ======")

    # Automatically get today's date
    today = datetime.now().strftime("%Y-%m-%d")
    print("Date: " + today)

    # This list will hold all the exercises the user enters
    exercises = []

    # Keep asking for exercises until the user types "done"
    while True:
        print("\nEnter exercise name (or type 'done' to finish):")
        name = input("Exercise: ").strip()

        if name.lower() == "done":
            break

        if name == "":
            print("Exercise name cannot be empty. Try again.")
            continue

        # Get the sets, reps and weight from the user
        sets = int(input("Sets: "))
        reps = int(input("Reps: "))
        weight = float(input("Weight in kg (enter 0 for bodyweight): "))

        # Calculate the volume for this exercise
        volume = calculate_volume(sets, reps, weight)

        # Store this exercise as a dictionary
        exercise = {
            "name": name,
            "sets": sets,
            "reps": reps,
            "weight": weight,
            "volume": volume
        }

        exercises.append(exercise)
        print("Logged: " + name + " | Volume: " + str(volume))

    # If no exercises were entered, cancel the session
    if len(exercises) == 0:
        print("No exercises entered. Session cancelled.")
        return

    # Create a new WorkoutSession object using our class
    new_session = WorkoutSession(today, exercises)

    # Check for personal bests before saving
    check_personal_bests(sessions, new_session)

# Convert the session to a dictionary and add it to our list
    sessions.append(new_session.to_dictionary())

    # Save all sessions to the file
    save_sessions(sessions)

    print("Total session volume: " + str(new_session.get_total_volume()))


