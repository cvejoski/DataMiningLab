'''
Created on Jan 22, 2015

@author: kostadin
'''

import numpy as np
import math

def normalization(x, min_x, max_x):
    return float(x - min_x)/float(max_x - min_x)

def euclidean_distance_square(x, y):
    assert len(x) == len(y)    
    diff = x - y
    return np.dot(diff, diff)

def chunker(seq, size):
    return (seq[pos:pos + size] for pos in xrange(0, len(seq), size))

def check_ball_angle(angle, epsilon):
    if -1 <= angle and angle <= epsilon:
        return True
    return False

def cos_of_angle_between(v1, v2):
    """ Returns cos of angle between vectors 'v1' and 'v2'    """
    assert len(v1) == len(v2)
    return np.dot(v1, v2)/(np.linalg.norm(v1)*np.linalg.norm(v2))

def calculate_period(first_half_start, first_half_end, second_half_start, second_half_end, current_time):
    if current_time > first_half_start and current_time < first_half_end:
        current_second = (current_time - first_half_start) / 1000000000000.
        return 1, int(math.ceil(current_second / 60.))
    if current_time > second_half_start and current_time < second_half_end:
        current_second = (current_time - second_half_start) / 1000000000000.
        return 2, int(math.ceil(current_second / 60.))
    return 0, 0