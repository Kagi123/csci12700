#Name: Sangheum Park
#Email:sangheum.park27@myhunter.cuny.edu
#Date: February 13, 2022
#a program that asks the user for a noun and two verbs

import matplotlib.pyplot as plt
import numpy as np

num = int(input('Enter size'))
img = np.ones((num,num,3))
img[::2,:1:] = 0
plt.imshow(img)
