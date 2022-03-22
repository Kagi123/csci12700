#Name: Sangheum Park
#Email:sangheum.park27@myhunter.cuny.edu
#Date: March 21, 2022
#asks the user for the hour of the day (in 24 hour time), and prints
#"Good Morning" if it is strictly before 12,
#"Good Afternoon" if it is 12 or greater, but strictly before 17, and
#"Good Evening" otherwise.

hours = int(input("Enter hour (in 24 hour time): "))

if hours < 12:
  print("Good Morning")
elif hours < 17:
  print("Good Afternoon")
else:
  print("Good Evening")




