'''
Created on Mar 2, 2015

@author: kostadin
'''

from helper.normalization import chunker
from helper.normalization import calculate_period
from pandas import  DataFrame

STANDING = 1 * 1/3.6
TROT = 11 * 1/3.6
RUN = 14 * 1/3.6
SPEED_RUN = 17 * 1/3.6
HIGH_SPEED_RUN = 24 * 1/3.6

def calc_intensity(speed):
    if speed <= STANDING:
        return 0
    if speed <= TROT:
        return 1
    if speed <= RUN:
        return 2
    if speed <= SPEED_RUN:
        return 3
    if speed <= HIGH_SPEED_RUN:
        return 4
    else:
        return 5


def __calculate_running_statistics(team, chunk):
    current_running_statistics = []
    it = team.iterrows()
    for index, row in it:
        curr_player_chunk = chunk[(chunk.sid == row.LL) | (chunk.sid == row.RL)]
        for i in chunker(curr_player_chunk, 16):
            speed = i.v.mean()/1000000
            ts_start = i.ts.min()
            ts_end = i.ts.max()
            distance = (speed*(ts_end-ts_start)/1000000000000)
            half, minute = calculate_period(10753295594424116, 12557295594424116, 13086639146403495, 14879639146403495, ts_start)
            current_running_statistics.append([half, minute, ts_start, ts_end, ts_end-ts_start, row.ID, calc_intensity(speed), speed, distance])

    return current_running_statistics

def current_running_statistics(reader, TeamA, TeamB):
    rs_teamA = []
    rs_teamB = []
    for chunk in reader:
        #calculate for Team A    
        rs_teamA.extend(__calculate_running_statistics(TeamA, chunk))
        print "A" + str(len(rs_teamA))
        #calculate for Team B
        rs_teamB.extend(__calculate_running_statistics(TeamB, chunk))
        print "B" + str(len(rs_teamB))
        
    dfA = DataFrame(rs_teamA, columns=['period', 'minute', 'ts_start', 'ts_end', 'time', 'player_id', 'intensity', 'speed', 'distance'])
    dfB = DataFrame(rs_teamB, columns=['period', 'minute', 'ts_start', 'ts_end', 'time', 'player_id', 'intensity', 'speed', 'distance'])
    
    return dfA, dfB

def aggregate_running_performance(team, data, window_size):
    team_it = team.iterrows()
    total = []
    for player_index, player_row in team_it:    
        A1 = data[data.player_id == player_row.ID]
        
        total_per_player = []
        for per in range(1, 3):
            counter = 1
            for i in chunker(A1[(A1.period == per)], 1500*window_size):
                total_per_window = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
                for j in chunker(i, 25):
                    grouped = j.groupby(i['intensity'])
                    summed = grouped.sum()
                    it = summed.iterrows()
                    for index, row in it:
                        total_per_window[index][0] += row.time / 1000000000000
                        total_per_window[index][1] += row.distance
                    total_per_player.append([player_row.ID, per, counter, total_per_window[0][0], total_per_window[0][1],
                                  total_per_window[1][0],total_per_window[1][1],total_per_window[2][0],total_per_window[2][1],
                                  total_per_window[3][0],total_per_window[3][1],total_per_window[4][0],total_per_window[4][1],
                                  total_per_window[5][0],total_per_window[5][1]])
                counter += 1
        total.extend(total_per_player)
    return DataFrame(total, columns=['player_id', 'period', 'window',
                                       'standing_time', 'standing_distance',
                                       'tort_time', 'tort_distance',
                                       'run_time', 'run_distance',
                                       'speed_run_time', 'speed_run_distance',
                                       'high_speed_run_time', 'hihg_speed_run_distance',
                                       'sprint_run_time', 'sprint_distance'])