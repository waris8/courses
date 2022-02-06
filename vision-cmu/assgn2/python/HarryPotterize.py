import numpy as np
import cv2
import skimage.io 
import skimage.color
from matchPics import matchPics
from planarH import computeH_ransac
#Import necessary functions

#Write script for Q2.2.4
cv_cover = skimage.io.imread("../data/cv_cover.jpg")
# skimage.io.imshow(cv_cover)
cv_desk = skimage.io.imread("../data/cv_desk.png")
# skimage.io.imshow(cv_desk)
hp_cover = skimage.io.imread("../data/hp_cover.jpg")

matches, locs1, locs2 = matchPics(cv_cover, cv_desk)
matches = np.hstack((matches.T, np.ones((2,1),np.int64))).T
n = matches.shape[0]
x1 = np.array([locs1[i] for i in matches[:,0]])
x2 = np.array([locs2[i] for i in matches[:,1]])
H2to1, inliers  = computeH_ransac(x1, x2)
warped_image = skimage.transform.warp(hp_cover, H2to1)
skimage.io.imshow(warped_image)
