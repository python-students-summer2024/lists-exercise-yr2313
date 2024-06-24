import datetime
def assess_mood():
    f = open("data/mood_diary.txt", encoding="utf-8", mode="a+") # open + create file
    date_today = str(datetime.date.today()) # get today's date

#check if already completed today
    f.seek(0)
    entries = f.readlines()
    for entry in entries:
         if date_today in entry:
                print("Sorry, you have already entered your mood today.")
                return 

# get mood
    mood = input("Enter your mood: ")
    num_mood = 0
    while not mood in ["happy", "relaxed", "apathetic", "sad", "angry"]:
        mood = input("Enter your mood: ")
    if mood == "happy":
        num_mood = 2
    elif mood == "relaxed":
        num_mood = 1
    elif mood == "apathetic":
        num_mood = 0
    elif mood == "sad":
        num_mood = -1
    elif mood == "angry":
        num_mood = -2

#store data
    f.write(f"{date_today}: {num_mood}\n")
    f.seek(0)
    entries = f.readlines()
    if len(entries) >= 7:
        mood_entries = []
        for entry in entries [-7: ]:
            sep_mood = int(entry.split(": ")[1])
            mood_entries.append(sep_mood)

# determining diagnosis
    # average mood by default
        total_mood = sum(mood_entries)
        average_mood = round(total_mood/7)
        if average_mood == 2:
            diagnosis = "happy"
        elif average_mood == 1:
            diagnosis = "relaxed"
        elif average_mood == 0:
            diagnosis = "apathetic"
        elif average_mood == -1:
            diagnosis = "sad"
        elif average_mood == -2:
            diagnosis = "angry"

    # changing diagnosis from default
        amount_happy = 0
        amount_sad = 0
        amount_apathetic = 0

        for mood in mood_entries:
            if mood == 2:
                amount_happy += 1
            if mood == -1:
                amount_sad += 1
            elif mood == 0:
                amount_apathetic += 1

        if amount_happy >= 5:
            diagnosis = "manic"
        elif amount_sad >= 4:
            diagnosis = "depressive"
        elif amount_apathetic >= 6:
            diagnosis = "schizoid"
    
    # print diagnosis
        print(f"Your diagnosis: {diagnosis}!")

        f.close() # close file