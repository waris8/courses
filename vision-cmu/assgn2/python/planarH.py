import numpy as np
import cv2


def computeH(x1, x2):
	#Q2.2.1
	#Compute the homography between two sets of points
    N = x1.shape[0]
    A = np.zeros(2*N,9)
    for i in range(N):
        A[i:i+1,:] = mat(x1[i,0],x2[i,0],x1[i,1],x2[i,1])
    
    eigenValues = np.linalg.eig(np.dot(A,A))
    

	return H2to1

def mat(x1,x2,y1,y2):
    output = np.array([[x1,y1,1,0,0,0,-x1*x2,-y1*x2,-x1],[0,0,0,x1,y1,1,-x1*y2,-y1*y2,-y2]])
    return output
    

def computeH_norm(x1, x2):
	#Q2.2.2
	#Compute the centroid of the points


	#Shift the origin of the points to the centroid


	#Normalize the points so that the largest distance from the origin is equal to sqrt(2)


	#Similarity transform 1


	#Similarity transform 2


	#Compute homography


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

