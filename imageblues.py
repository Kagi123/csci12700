#Name: Sangheum Park
#Email:sangheum.park27@myhunter.cuny.edu
#Date: February 13, 2022
#create a new image that
#has only the blue channel of the original image.

import matplotlib.pyplot as plt
import numpy as np

image = input("Enter name of the input file: ")
img = plt.imread(image)

   
                       
img2 = img.copy()       
img2[:,:,1] = 0         
img2[:,:,0] = 0          
image2 = input("Enter name of the output file: ")
plt.imsave(image2, img2)
