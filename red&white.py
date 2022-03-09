#Name: Sangheum Park
#Email:sangheum.park27@myhunter.cuny.edu
#Date: March 01, 2022
#This program creates a image of red and white stripes. 
import matplotlib.pyplot as plt
import numpy as np

num = int(input("Enter size: "))
name = input('Enter output file: ')

img = np.ones((num,num,3))
img[::2,:,1:] = 0


plt.imsave(name,img)
plt.show()




