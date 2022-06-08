from datetime import datetime

today = datetime.now().strftime("%A")
print(today)
#today = "Saturday"

#check if today is a weekday
if today in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    print("Today is a weekday")
elif today in ["Saturday", "Sunday"]:
    print("Today is a weekend")


