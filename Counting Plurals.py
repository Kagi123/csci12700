#Name: Sangheum Park
#Email:sangheum.park27@myhunter.cuny.edu
#Date: March 09, 2022
#Counting Plurals

nouns = input("Enter nouns: ")

words = nouns.split(' ')
num = 0
plural = 0.0
abc = "abc"

for word in words:
  num += 1
  i = len(word)
  if(word[i-1] == 's' and word[i-2] != 'e'):
    plural += 0.5
print("num items: ", num)
print(" fraction plural: ", plural)
