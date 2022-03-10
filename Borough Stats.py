#Name: Sangheum Park
#Email:sangheum.park27@myhunter.cuny.edu
#Date: March 10, 2022
#TurtleString

import matplotlib.pyplot as plt
import pandas as pd

#Open the CSV file and store in pop
pop = pd.read_csv('nycHistPop.csv',skiprows=5)
borough = input("Enter borough name: ")

print('Average population: ',pop[borough].mean())
print('Maximum population:  ',pop[borough].max())


