# workout.py
# Project 9 - Workout Tracker
# Tech4Girls Backend Cohort 4


import datetime # automatically capture today's date.
def save_sessions(sessions):   
    file = open("workouts.txt", "w") # opens file called works.txt inw write mode
    file.write(str(sessions)) # changes session list into string and saves it into file
    file.close() # closes file after

def load_sessions():
    try:
        file = open("workouts.txt", "r")  #opens file called works.txt in read mode
        data = file.read()  #reads content of  file
        file.close()
        return eval(data) # changes text back to python list
    except:
        return [] # if file does not exist, return an empty list



def log_session(sessions):

    exercises = [] # create an empty list for storing exercises in woerkout session

    while True: # for multiple exercise addition

        name = input("Exercise name (or end): ") # request user for name  or end to stop asking

        if name == "end":  #stops adding exercise if user types end
            break  

        sets = int(input("Sets: ")) # askes user for number of sets
        reps = int(input("Reps: ")) # askes user for number of reps
        weight = float(input("Weight (0 for bodyweight): ")) # askes user for weight used

        exercise = { # create a dictionary to store eexercise information
            "name": name,
            "sets": sets,
            "reps": reps,
            "weight": weight
        }

        exercises.append(exercise) # adds exercise dictionary to exercise list


    session = { # add session dictionary
        "date": str(datetime.date.today()), # automatically stores date
        "exercises": exercises # stores all exercises in session
    }

    sessions.append(session) # adds session to list of sessions

    return session # returns a new session

def calculate_volume(exercise): # function for volume calculation

    weight = max(exercise["weight"], 1) # fi weight =0 for bodyweight , use 1 instead

    return exercise["sets"] * exercise["reps"] * weight # calculates exercise volume


def view_all_sessions(sessions): #function for viewing sessions

    for session in sessions: # loops through all saved workout sessions

        total_volume = 0 #resets total volume for each session

        for exercise in session["exercises"]: # loop through exercises in session
            volume = calculate_volume(exercise) 
            total_volume += calculate_volume(exercise) # adds exercise volume to total

        print("Date:", session["date"]) # prints session date
        print("Total Volume:", total_volume) # prints total volume 
   

def check_personal_bests(sessions, new_session):
    # Loop through each exercise in the new session
    for exercise in new_session["exercises"]:
        # Calculate the volume of the current exercise
        new_volume = calculate_volume(exercise)

        # Track the highest volume seen so far for this exercise
        best_volume = 0
    for session in sessions:
        for old_exercise in session["exercises"]:
                if old_exercise["name"] == exercise["name"]:
                    old_volume = calculate_volume(old_exercise)
                if old_volume > best_volume:
                        best_volume = old_volume

        # Compare new volume with best volume
        if new_volume > best_volume:
            print(f"New Personal Best for {exercise['name']}!")
