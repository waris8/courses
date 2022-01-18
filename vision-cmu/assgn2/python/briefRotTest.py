import numpy as np
import cv2
from matchPics import matchPics
import scipy as sc
import matplotlib.pyplot as plt

#Q2.1.5
#Read the image and convert to grayscale, if necessary
img = cv2.imread('../data/cv_cover.jpg')
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
noOfMatches = np.zeros(36)
bins = []
for i in range(36):
	#Rotate Image
    rotated = sc.ndimage.rotate(imgGray, i*10)
	#Compute features, descriptors and Match features
    matches, locs1, locs2 =matchPics(imgGray,rotated)
	#Update histogram
    noOfMatches[i] = matches.shape[0]
    bins.append(i*10)

#Display histogram
fig, axs = plt.subplots(1, 1,
                        figsize =(10, 7),
                        tight_layout = True)
axs.hist(noOfMatches,bins)
