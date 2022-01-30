import numpy as np
import cv2


def computeH(x1, x2):
	#Q2.2.1
	#Compute the homography between two sets of points
    N = x1.shape[0]
    A = np.zeros(2*N,9)
    for i in range(N):
        A[i:i+1,:] = mat(x1[i,0],x2[i,0],x1[i,1],x2[i,1])
    
    eigenValues, eigenVector = np.linalg.eig(np.dot(A,A))
    temp = 0
    
    for j in range(9):
        if eigenValues[j] < temp:
            temp = j
            
    h = eigenVector[:,temp]
    H2to1 = np.zeros(3,3)
    H2to1[0,:] = h[:2]
    H2to1[1,:] = h[3:5]
    H2to1[2,:] = h[6:8]
    
    return H2to1

def mat(x1,x2,y1,y2):
    output = np.array([[x1,y1,1,0,0,0,-x1*x2,-y1*x2,-x1],[0,0,0,x1,y1,1,-x1*y2,-y1*y2,-y2]])
    return output
    

def computeH_norm(x1, x2):
	#Q2.2.2
	#Compute the centroid of the points
    x1_mean = np.average(x1,axis=1)
    x2_mean = np.average(x2,axis=1)
    
	#Shift the origin of the points to the centroid
    x1_shifted = x1 - x1_mean
    x2_shifted = x2 - x2_mean

	#Normalize the points so that the largest distance from the origin is equal to sqrt(2)
    s1_max = np.max([np.sqrt(x1[i,0]**2 + x1[i,1]**2) for i in range(x1.shape[0])])
    s2_max = np.max([np.sqrt(x2[i,0]**2 + x2[i,1]**2) for i in range(x2.shape[0])])
    x1_shifted *= (np.sqrt(2)/s1_max)
    x2_shifted *= (np.sqrt(2)/s2_max)
    
	#Similarity transform 1
    

	#Similarity transform 2


	#Compute homography
    H_norm = computeH(x1_shifted, x2_shifted)

	#Denormalization
	

	return H2to1




def computeH_ransac(locs1, locs2):
	#Q2.2.3
	#Compute the best fitting homography given a list of matching points



	return bestH2to1, inliers



def compositeH(H2to1, template, img):
	
	#Create a composite image after warping the template image on top
	#of the image using the homography

	#Note that the homography we compute is from the image to the template;
	#x_template = H2to1*x_photo
	#For warping the template to the image, we need to invert it.
	

	#Create mask of same size as template

	#Warp mask by appropriate homography

	#Warp template by appropriate homography

	#Use mask to combine the warped template and the image
	
	return composite_img


