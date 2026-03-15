# workout.py
# Project 9 - Workout Tracker
# Tech4Girls Backend Cohort 4


import datetime
def save_sessions(sessions):
    file = open("workouts.txt", "w")
    file.write(str(sessions))
    file.close()

def load_sessions():
    try:
        file = open("workouts.txt", "r")
        data = file.read()
        file.close()
        return eval(data)
    except:
        return []



def log_session(sessions):

    exercises = []

    while True:

        name = input("Exercise name (or done): ")

        if name == "done":
            break

        sets = int(input("Sets: "))
        reps = int(input("Reps: "))
        weight = float(input("Weight (0 for bodyweight): "))

        exercise = {
            "name": name,
            "sets": sets,
            "reps": reps,
            "weight": weight
        }

        exercises.append(exercise)

    session = {
        "date": str(datetime.date.today()),
        "exercises": exercises
    }

    sessions.append(session)

    return session

