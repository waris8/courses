import numpy as np
import cv2
import skimage.color
from helper import briefMatch
from helper import computeBrief
from helper import corner_detection

def matchPics(I1, I2):
    #I1, I2 : Images to match
    #Convert Images to GrayScale
    img1 = skimage.color.rgb2gray(I1)
    img2 = skimage.color.rgb2gray(I2)
    #Detect Features in Both Images
    locs1 = corner_detection(img1)
    locs2 = corner_detection(img2)
    #Obtain descriptors for the computed feature locations
    brief1, locs1Updated = computeBrief(img1,locs1)
    brief2, locs2Updated = computeBrief(img2,locs2)
    #Match features using the descriptors
    matches = briefMatch(brief1,brief2)

    return matches, locs1, locs2
