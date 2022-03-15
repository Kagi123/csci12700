#Name: Sangheum Park
#Email:sangheum.park27@myhunter.cuny.edu
#Date: March 13, 2022
#displays shelter population over time
#store the plot in the output file the user specified

import matplotlib.pyplot as plt
import pandas as pd

f = input("Enter name of input file: ")
homeless = pd.read_csv(f)

homeless['Fraction Children'] = homeless['Total Children in Shelter']/homeless['Total Individuals in Shelter']
homeless['Fraction Single Adults'] = 1 - homeless['Fraction Children']
homeless.plot(x = 'Date of Census', y = 'Fraction Single Adults')

name = input("Enter output file name: ")
fig = plt.gcf()
fig.savefig(name)
