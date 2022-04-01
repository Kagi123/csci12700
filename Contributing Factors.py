#Name: Sangheum Park
#Email:sangheum.park27@myhunter.cuny.edu
#Date: April 1, 2022
#list the top three contributing factors for the primary #vehichle of collisions ("CONTRIBUTING FACTOR VEHICLE 1") in the #file.


import pandas as pd

csvFile = input('Enter CSV file name: ')         #Name of the CSV file
factors = pd.read_csv(csvFile)     #Read in the file to a dataframe

print("Top three contributing factors for collisions:")

print(factors["CONTRIBUTING FACTOR VEHICLE 1"].value_counts()[:3]) 