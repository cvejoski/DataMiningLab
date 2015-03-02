'''
Created on Jan 25, 2015

@author: kostadin
'''
import numpy as np
from numpy import linalg
import math
import sys

def calculate_center(snapshots):
    return np.sum(snapshots, axis=0)/len(snapshots)

def calculate_covariance(snapshots, center, alpha, sigma_min):
    covariance = np.dot((np.array(snapshots) - center).T, np.array(snapshots) - center)
    
    #check if matrix is singular and handle it
    if not (linalg.cond(covariance) < 1/sys.float_info.epsilon):
        if (np.matrix.trace(covariance) > 0):
            covariance = (1 - alpha) * covariance + alpha * np.matrix.trace(covariance) / 2. * np.identity(2)
        else:
            covariance = (1 - alpha) * covariance + alpha * sigma_min * np.identity(2)
    return covariance

def spatial_kernel(snapshots_x, snapshots_y):
    result = 0.
    for i in range(1, len(snapshots_x)):
        centers = [calculate_center(snapshots_x[i]), calculate_center(snapshots_y[i])]
        covariances = [calculate_covariance(snapshots_x[i], centers[0], 0.1, 0.1), calculate_covariance(snapshots_y[i], centers[1], 0.1, 0.1)]
        result += probability_product_kernel(covariances, centers)
    return result / float(len(snapshots_x)-1)

def temporal_kernel(t_1, t_2, sigma):
    return np.exp(1./(2*sigma**2) * (t_1-t_2)**2)

def probability_product_kernel(covariances, centers):
    sigma_star = linalg.inv(linalg.inv(covariances[0]) + linalg.inv(covariances[1]))
    center_star = np.dot(linalg.inv(covariances[0]), centers[0].T) + np.dot(linalg.inv(covariances[1]), centers[1].T)
    result = 2*math.sqrt(linalg.det(sigma_star))*math.pow(linalg.det(covariances[0]), -1./4.)*math.pow(linalg.det(covariances[1]), -1./4.)*\
        math.exp(-1./4.*(np.dot(np.dot(centers[0], linalg.inv(covariances[0])), centers[0].T) + np.dot(np.dot(centers[1], linalg.inv(covariances[1])), centers[1].T) +\
                         np.dot(np.dot(center_star, linalg.inv(sigma_star)), center_star.T)))
    return result

def r_kernel(trajectory_x, trajectory_y):
    result = 0.
    for i in range(len(trajectory_x)):
        for j in range(len(trajectory_y)):
            result += temporal_kernel(trajectory_x[i][0], trajectory_y[j][0], 0.5)*spatial_kernel(trajectory_x[i], trajectory_y[j])
    return result / float(len(trajectory_x)*len(trajectory_y))