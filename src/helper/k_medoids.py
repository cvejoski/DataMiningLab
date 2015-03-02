'''
Created on Jan 26, 2015

@author: kostadin
'''
import numpy as np

import big_game.tacktick_extraction as te

def clustering(points, num_of_clusters):
    distance_matrix = __distance_matrix(points)
    medoids = np.random.randint(0, len(points), num_of_clusters)
    new_medoids = np.ones(num_of_clusters)
    for i in range(100):
        medoids = np.random.randint(0, len(points), num_of_clusters)
        new_medoids = np.ones(num_of_clusters)
        checking = True
        while checking:
            clusters = __assign_cluster(points, medoids, distance_matrix)    
            new_medoids = __calculate_medoids(points, clusters, num_of_clusters, distance_matrix)
            if (np.allclose(new_medoids, medoids)):
                checking = False
            medoids = new_medoids
        print i, new_medoids, clusters, __inter_cluster_distance(clusters, num_of_clusters, distance_matrix)
    return new_medoids, clusters
    
def __assign_cluster(points, medoids, distance_matrix):
    clusters = np.ones(len(points))*-1
    for p in range(len(points)):
        min_dist = np.ones(len(medoids))*10e9
        for m in range(len(medoids)):
            min_dist[m] = distance_matrix[p][int(medoids[m])]
        clusters[p] = np.argmin(min_dist, 0)
    return clusters

def __calculate_medoids(points, clusters, num_clusters,  distance_matrix):    
    medoids = np.ones(num_clusters)*-1
    for i in range(num_clusters):
        min_dist = 10e9
        min_dist_id = -1 
        for j in range(len(clusters)):
            if clusters[j] == i:
                for k in range(len(clusters)):
                    if clusters[k] == i:
                        min_dist_tmp = distance_matrix[j][k]
#                         min_dist_tmp = __distance(points[j], points[k])
                        if (min_dist_tmp < min_dist):
                            min_dist = min_dist_tmp
                            min_dist_id = j
        medoids[i] = min_dist_id
    return medoids

def __distance(x, y):
    return te.r_kernel(x, x) - 2*te.r_kernel(x, y) + te.r_kernel(y, y)

def __distance_matrix(points):
    n_points = len(points)
    result = np.zeros(n_points**2).reshape((n_points, n_points))  
    for i in range(n_points):
        for j in range(i, n_points):
            result[i][j] = result[j][i] = __distance(points[i], points[j])
    return result

def __inter_cluster_distance(cluster, num_clusters, distance_matrix):
    inter_distance = 0
    for i in range(num_clusters):
        for j in range(len(cluster)):
            if (cluster[j] == i):
                for k in range(len(cluster)):
                    if (cluster[k] == i):
                        inter_distance += distance_matrix[j][k]
    return inter_distance
            