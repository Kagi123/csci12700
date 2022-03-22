#Name: Sangheum Park
#Email:sangheum.park27@myhunter.cuny.edu
#Date: March 21, 2022
#Ask the user for the name of the input file.
#Ask the user for the attribute (column header) to search by.


import pandas as pd

csvFile = input('Enter CSV file name: ')         #Name of the CSV file
tickets = pd.read_csv(csvFile)     #Read in the file to a dataframe

attribute = input("Enter attribute:")

print("The 10 worst offenders are:")

print(tickets[attribute].value_counts()[:10]) 



