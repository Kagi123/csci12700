#Name: Sangheum Park
#Email:sangheum.park27@myhunter.cuny.edu
#Date: March 21, 2022
#print out the names,
#one per line, with the first names first followed by the last names..

names = input("Please enter your list of names:")
name = names.split(";")
print()
print("You entered: ")
for aname in name:
  abc = aname.split(",")
  result = ""
  for name in abc:
    result = name + result
  print(result)

print()

print("Thank you for using my name organizer!")




