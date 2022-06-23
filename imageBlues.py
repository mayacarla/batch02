#Maya Carla Loleatha Anderson
#maya.anderson86@myhunter.cuny.edu
#this program prints: two images, one with RGB and one without RG

import matplotlib.pyplot as plt
import numpy as np


inputFile = input("Enter name of the input file: ")

img = plt.imread(inputFile)


img2 = img.copy()
img2[:, :, 0] = 0
img2[:, :, 1] = 0


outputFile = input("Enter name of the output file: ")
plt.imsave(outputFile, img2)



