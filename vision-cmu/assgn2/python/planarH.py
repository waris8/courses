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
    # x1_shifted = x1 - x1_mean
    # x2_shifted = x2 - x2_mean 
    trans_mat_1 = np.array([0,0,-x1_mean[0]],[0,0,-x1_mean[1]],[0,0,1])
    trans_mat_2 = np.array([0,0,-x2_mean[0]],[0,0,-x2_mean[1]],[0,0,1])
	#Normalize the points so that the largest distance from the origin is equal to sqrt(2)
    s1_max = np.max([np.sqrt(x1[i,0]**2 + x1[i,1]**2) for i in range(x1.shape[0])])
    s2_max = np.max([np.sqrt(x2[i,0]**2 + x2[i,1]**2) for i in range(x2.shape[0])])
    scale_mat_1 = np.array([s1_max,0,0],[0,s1_max,0],[0,0,1])
    scale_mat_2 = np.array([s2_max,0,0],[0,s2_max,0],[0,0,1])
    # x1_shifted *= (np.sqrt(2)/s1_max)
    # x2_shifted *= (np.sqrt(2)/s2_max)
	#Similarity transform 1
    T1 = np.matmul(trans_mat_1,scale_mat_1)
    x1_hom = np.hstack(x1,np.ones(x1.shape[0],1))
    x1_trans = np.matmul(T1,x1_hom)
	#Similarity transform 2
    T2 = np.matmul(trans_mat_2,scale_mat_2)
    x2_hom = np.hstack((x2,np.ones(x2.shape[0],1)))
    x2_trans = np.matmul(T2,x2_hom)
	#Compute homography
    H_norm = computeH(x1_trans, x2_trans)
	#Denormalization
    H2to1 = np.matmul(np.linalg.inv(T1),np.dot(H_norm,T2))
    return H2to1




def computeH_ransac(locs1, locs2):
	#Q2.2.3
	#Compute the best fitting homography given a list of matching points
    N = locs1.shape[0]
    k = 20
    t = 1
    inliers = np.zeros(N,1)
    bestH2to1 = np.zeros
    for i in range(k):
        n = np.random.randint(0,N,size=4)
        x1 = np.array([locs1[i] for i in range(n)])
        x2 = np.array([locs2[i] for i in range(n)])
        H2to1 = computeH_norm(x1,x2)
        temp_inliers = np.zeros(N,1)
        for j in range(N):
            x2_calc = compute_x2(locs1[j],H2to1)
            l2_distance = np.linalg.norm(locs2[j]-x2_calc)
            if l2_distance < t:
                temp_inliers[j] = 1
        if np.sum(temp_inliers) > np.sum(inliers):
            inliers = temp_inliers
            bestH2to1 = H2to1
    return bestH2to1, inliers

def compute_x2(x1, H2to1):
    x1 = np.hstack((x1,1))
    x2 = np.dot(H2to1,x1)
    x2 = x2/x2[2]
    return x2[:1]

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


