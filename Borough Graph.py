#Name: Sangheum Park
#Email:sangheum.park27@myhunter.cuny.edu
#Date: March 09, 2022
#display the fraction of the population
#that has lived in that borough, over time.

import matplotlib.pyplot as plt
import pandas as pd

#Open the CSV file and store in pop
pop = pd.read_csv('nycHistPop.csv',skiprows=5)
borough = input("Enter borough name: ")
#Compute the fraction of the population in the borough, and save as new column:
pop['Fraction'] = pop[borough]/pop['Total']

#Create a plot of year versus fraction of pop. in borough (with labels):
pop.plot(x = 'Year', y = 'Fraction')

fig = plt.gcf()
name = input("Enter output file name: ")
fig.savefig(name)
