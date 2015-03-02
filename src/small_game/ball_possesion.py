'''
Created on Mar 2, 2015

@author: kostadin
'''

import math
from pandas import  DataFrame
from helper.normalization import calculate_period
from helper.normalization import euclidean_distance_square
import numpy as np

GOAL_AREA_1 = {'X_MIN': 22578.5, 'X_MAX': 29898.5, 'Y': 33941.0, 'Z_MAX': 2440.}
GOAL_AREA_2 = {'X_MIN': 22560., 'X_MAX': 29880., 'Y': -33968.0, 'Z_MAX': 2440.}
TIME = 1.5
GRAVITY = 9.81 * 1e3

def shots_on_goal(data):
    shots_on_goal = []
    first = data[data.period != 0]
    first_it = first.iterrows()
    
    for index, row in first_it:  
        if (row.a / 10e6 >= 55.):
            factor = 1e4 * 1e6
            vx = row.v * row.vx / factor
            vy = row.v * row.vy / factor
            vz = row.v * row.vz / factor
            proj_x = vx * TIME + row.x
            proj_y = vy * TIME + row.y
            proj_z = vz * TIME + row.z #- (0.5 * GRAVITY * TIME * TIME)
           
            if __check_goal_hit(row, proj_x, proj_y, proj_z) == True:
                shots_on_goal.append([row.period, row.minute, row.ts, row.team, row.player_id, row.x, row.y])
    
    return shots_on_goal

def extract_passess(ball_possession):
    result_passes = []
    first = ball_possession[ball_possession.period != 0]
    first_it = first.iterrows()
    
    check = True
    for index, row in first_it:  
        if (row.a / 1000000. >= 55.) and (check == True):
            first_row = row
            check = False
        if row.player_id != first_row.player_id:
            future_g = ball_possession.ix[index:index + 35].groupby(ball_possession['player_id'])
            if future_g.count().ix[row.player_id].period >= 35:
                check = True
                success = ""
                if first_row.team == row.team:
                    success = "completed"
                else:
                    success = "faild"
           
                result_passes.append([row.period, row.minute, row.team, success, first_row.ts, 
                                      first_row.player_id, row.player_id, first_row.x, first_row.y, row.x, row.y])
                first_row = row
    return DataFrame(result_passes, columns=['period', 'minute', 'team', 'result', 'ts', 'first_player', 
                                             'second_player', 'x_1', 'y_1', 'x_2', 'y_2'])

def extract_ball_possession(reader, TeamA, TeamB, balls):
    counter = 1
    result = []
    for T in reader:
        print counter
        counter += 1
        ball_data = T[T.sid.isin(balls) & (T.x >= 0) & (T.x <= 52483) & 
                                  (T.y >= -33960) & (T.y <= 33965)][::80]
        player_data = T[~T.sid.isin(balls)]
        
        player_id = ""
        team = 0
        ball_row_old = ball_data.ix[0:1]
        
        ball_it = ball_data.iterrows()
        for ball_index, ball_row in ball_it:
        
            half, minute = calculate_period(10753295594424116, 12557295594424116, 13086639146403495, 14879639146403495, ball_row.ts)
            if ball_row.a / 1e6 >= 55.: 
                p = player_data[(player_data.ts <= ball_row.ts + 15e11)
                            & (player_data.ts >= ball_row.ts - 15e11)]
                half, minute = calculate_period(10753295594424116, 12557295594424116, 13086639146403495, 14879639146403495, ball_row.ts)
                player_id_tmp, team_tmp, prox = __player_distance(TeamA, TeamB, p, ball_row)
                if prox == True:
                    player_id = player_id_tmp
                    team = team_tmp
            result.append([half, 
                           minute,
                           player_id,
                           team,
                           ball_row.sid,
                           ball_row.ts, 
                           ball_row.x,
                           ball_row.y,
                           ball_row.z,
                           ball_row.v,
                           ball_row.a,
                           ball_row.vx,
                           ball_row.vy,
                           ball_row.vz,
                           ball_row.ax,
                           ball_row.ay,
                           ball_row.az])
            ball_row_old = ball_row
    return DataFrame(result, columns=['period', 'minute', 'player_id', 'team', 'sid', 'ts', 'x', 'y', 'z', 'v', 'a', 'vx', 'vy', 'vz', 'ax', 'ay', 'az'])
            
def __check_goal_hit(ball, x, y, z):   
    min_ = -33960  if ball.y > y else 33965
    ratio = (ball.y - min_) / (ball.y - y)
  
#     y = ball.y + (y - ball.y) * ratio
#     x = ball.x + (x - ball.x) * ratio
#     z = ball.z + (z - ball.z) * ratio   

#     z = max(z, 0)
  
    if (x > GOAL_AREA_1['X_MIN']) and (x < GOAL_AREA_1['X_MAX']) :#and (z > GOAL_AREA_1['Z_MAX']) :#and (ratio < 1) and (ratio >= 0):
        return True
    return False

def __player_distance(teamA, teamB, data_chunk, ball_row):
    distA, idA, prox_a = __team_player_distance(teamA, data_chunk, ball_row)
    distB, idB, prox_b = __team_player_distance(teamB, data_chunk, ball_row)
    if distA >= distB:
        return idB, 2, prox_b
    return idA, 1, prox_a

def __team_player_distance(team, data_chunk, ball_row):
    min_dist = 10000000000000
    min_id = ""
    min_time = 0
    #Iterate trouhgt all players
    it = team.iterrows()
    
    for player_index, player_row in it:
        curr_player_chunk = data_chunk[
                                       (data_chunk.sid == player_row.LL) | 
                                       (data_chunk.sid == player_row.RL)]
       
        if len(curr_player_chunk) > 0:
            #get row with ts clossest to ball ts        
            curr_play_row = curr_player_chunk.ix[((curr_player_chunk.ts - ball_row.ts).abs()).argmin()]
            
            #Calculate Euclidien distance
            dist = euclidean_distance_square(np.array([curr_play_row.x, curr_play_row.y, curr_play_row.z]), np.array(
                                                      [ball_row.x, ball_row.y, ball_row.z]))
            if min_dist > dist:
                min_dist = dist
                min_id = player_row.ID
            proximitiy = False
            if math.sqrt(min_dist) < 1000:
                proximitiy = True
    return min_dist, min_id, proximitiy
