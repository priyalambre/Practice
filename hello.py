day = input("enter your day : ")

if day == "Saturday" or day == "Sunday":
    print("It's the weekend! Time to relax.")
elif day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    print("It's a workday. Time to log in.")
else:
    print("Invalid day entered.")
