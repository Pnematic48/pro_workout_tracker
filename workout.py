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
    
    for exercise in new_session["exercises"]:    # Loop through each exercise in the new session
        new_volume = calculate_volume(exercise)   # Calculate the volume of the current exercise
        best_volume = 0 
        old_volume = 0                          # Track the highest volume seen so far for this exercise
    for session in sessions:
        for old_exercise in session["exercises"]:
                if old_exercise["name"] == exercise["name"]:
                    old_volume = calculate_volume(old_exercise)
                if old_volume > best_volume:
                        best_volume = old_volume

        
        if new_volume > best_volume:               # Compare new volume with best volume
            print(f"New Personal Best for {exercise['name']}!")
def weekly_summary(sessions):  
    today = datetime.date.today()                    # Get today’s date
    start_of_week = today - datetime.timedelta(days=today.weekday())  # Find the start of the current week (Monday)

    weekly_sessions = []
    total_volume = 0
    exercise_counter = {}

    for session in sessions:                    # Filter sessions that happened this week
        session_date = datetime.datetime.strptime(session["date"], "%Y-%m-%d").date()
        if session_date >= start_of_week:
            weekly_sessions.append(session)

            # Calculate total volume for this session
            session_volume = 0
            for exercise in session["exercises"]:
                volume = calculate_volume(exercise)
                session_volume += volume

                # Count how many times each exercise appears
                if exercise["name"] not in exercise_counter:
                    exercise_counter[exercise["name"]] = 0
                exercise_counter[exercise["name"]] += 1

            total_volume += session_volume

    # Print summary
    print("Weekly Summary:")
    print("Total Sessions:", len(weekly_sessions))
    print("Total Volume:", total_volume)

    if exercise_counter:
        most_trained = max(exercise_counter, key=exercise_counter.get)
        print("Most Trained Exercise:", most_trained)

    if weekly_sessions:
        avg_volume = total_volume / len(weekly_sessions)
        print("Average Session Volume:", avg_volume)

def view_session_by_date(sessions):
    # Ask user for a date
    date_input = input("Enter session date (YYYY-MM-DD): ")

    # Search for session with that date
    for session in sessions:
        if session["date"] == date_input:
            print("Session on", session["date"])
            for exercise in session["exercises"]:
                print(f"{exercise['name']} - Sets: {exercise['sets']}, Reps: {exercise['reps']}, Weight: {exercise['weight']}")
            return

    print("No session found for that date.")
def main():
    sessions = load_sessions()  # Load past sessions from file

    while True:
        print("\nWorkout Tracker Menu")
        print("1. Log a new session")
        print("2. View all sessions")
        print("3. Weekly summary")
        print("4. View session by date")
        print("5. Save and exit")

        choice = input("Choose an option: ")

        if choice == "1":
            new_session = log_session(sessions)
            check_personal_bests(sessions, new_session)
            sessions.append(new_session)

        elif choice == "2":
            view_all_sessions(sessions)

        elif choice == "3":
            weekly_summary(sessions)

        elif choice == "4":
            view_session_by_date(sessions)

        elif choice == "5":
            save_sessions(sessions)
            print("Sessions saved. Goodbye!")
            break

        else:
            print("Invalid choice, try again.")
if __name__ == "__main__":
    main()
