#Name: Sangheum Park
#Email:sangheum.park27@myhunter.cuny.edu
#Date: February 13, 2022
#piece of pseudocode as a complete program:

message = input("Enter a message: ")

for i in range(len(message)+1):
  print(message[0:i])

for i in range(len(message)+1):
  print(message[i+1:len(message)])

print("thank you")
