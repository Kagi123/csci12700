#Name: Sangheum Park
#Email:sangheum.park27@myhunter.cuny.edu
#Date: February 04, 2022
#This program prompts the user to enter a word 
#and then prints out the word 
#with each letter shifted right by 13. 
#That is, 'a' becomes 'n', 
#'b' becomes 'o', ... 'y' becomes 'l', and 'z' becomes 'm'.

word = input("Enter a word: ")

for i in word:
  if (ord(i) < 110):
    print(chr(ord(i)+13),end='')
  else  :
    print(chr(ord(i)-13),end='')

