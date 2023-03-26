date = input("Enter today's date: ")
mood = input("how do you feel today ? rate it outta /10: ")
thoughts = input("Let your thoughts flow: \n")

with open(f"journal/{date}.txt", "w") as file:
    file.write(mood + 2*"\n")
    file.write(thoughts)
