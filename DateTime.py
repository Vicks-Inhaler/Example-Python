# Program Python Date & Time

print()
print("========== Basic DateTime ==========")
import datetime

Date = datetime.date (2025, 1, 2)
Today = datetime.date.today()

Time = datetime.time (12, 30, 0)
Now = datetime.datetime.now()

print(Now)

# ========================================================================

print()
print("========== Example 1 DateTime ==========")
import datetime

Date = datetime.date (2025, 1, 2)
Today = datetime.date.today()

Time = datetime.time (12, 30, 0)
Now = datetime.datetime.now()

# Now = Now.strftime("%H:%M:%S %M %D %Y")
# Now = Now.strftime("%H:%M:%S %m %d %Y")
Now = Now.strftime("%H:%M:%S %m-%d-%Y")

print(Now)

# ========================================================================

print()
print("========== Example 2 DateTime ==========")
import datetime

Date = datetime.date (2025, 1, 2)
Today = datetime.date.today()

Time = datetime.time (12, 30, 0)
Now = datetime.datetime.now()

# Now = Now.strftime("%H:%M:%S %M %D %Y")
# Now = Now.strftime("%H:%M:%S %m %d %Y")
Now = Now.strftime("%H:%M:%S %m-%d-%Y")

Target_Datetime = datetime.datetime (2030, 1, 2, 12, 30, 1)
Target_Datetime1 = datetime.datetime (2020, 1, 2, 12, 30, 1)
Current_Datetime = datetime.datetime.now()
Current_Datetime1 = datetime.datetime.now()

if Target_Datetime < Current_Datetime :
    print("Target Date has Passed")
else :
    print("Target Date has Not Passed")

print()
if Target_Datetime1 < Current_Datetime1 :
    print("Target Date has Passed")
else :
    print("Target Date has Not Passed")