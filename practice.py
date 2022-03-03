import numpy as np
import matplotlib.pyplot as plt

logoimg = np.ones((10,10,3))
logoimg[:,:3,1] = 0

logoimg[:,-3,1] = 0
logoimg[4:6,:,1]=0
