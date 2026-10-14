#Student Marks
marks={"Alice": 85, "Bob": 30, "Charlie": 78, "Diana": 92, "Ethan": 34}
for i in marks:
    if marks[i] >= 40:
        print(i, "has passed with a score of", marks[i])
    else:
        print(i, "has failed with a score of", marks[i])