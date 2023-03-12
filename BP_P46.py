# Python Program

# Display Calendar of given month using Calendar Module

# import Module

import Calendar_Module

year = int(input("Enter Year: "))
month = int(input("Enter Month of Year: "))

print(f"Given {year} year and {month} month ")

print("Calendar is: ")

cal = Calendar_Module.Calendar_365(year=year, month=month)
cal.show()

# Thanks for Watching