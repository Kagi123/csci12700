#Name: Sangheum Park
#Email:sangheum.park27@myhunter.cuny.edu
#Date: March 15, 2022
#This program save the lower left quarter of the image
#to the output file specified by the user. 
import matplotlib.pyplot as plt
import numpy as np

inf = input("Enter image file name: ")
out_put = input('Enter output file: ')

img = plt.imread(inf) #read in image from inf

height = img.shape[0] #get height
width = img.shape[1] #get width

img2 = img[height//2:, :width//2]


plt.imsave(out_put,img2)
plt.show()




