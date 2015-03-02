'''
Created on Mar 2, 2015

@author: kostadin
'''

from helper.normalization import euclidean_distance_square
import big_game.schemes.player_stats1 as ps
import big_game.schemes.team_stats as ts
from pandas import  DataFrame, Series
from xml.dom import minidom
import pandas as pd
import numpy as np


def player_statistics(fileName):
    xml = open(fileName).read()
    # print xml
    data = ps.CreateFromDocument(xml)
    column_names = ['id', 'team_name', 'player_key', 'jersy', 'name', 'score', 'duels_won', 'duels_lost',
                'passes', 'passes_complited', 'on_target', 'off_target', 'assists', 'offsides', 
                'fouls_commited', 'fouls_suffered']
    player_stats = {}
    
    #per team
    for team in data.sports_event.team:    
        for player in team.player:
            player_stats.setdefault(column_names[0], []).append(team.team_metadata.id)
            player_stats.setdefault(column_names[1], []).append(team.team_metadata.name.full)
            player_stats.setdefault(column_names[2], []).append(player.player_metadata.player_key)
            player_stats.setdefault(column_names[3], []).append(player.player_metadata.uniform_number)
            player_stats.setdefault(column_names[4], []).append(player.player_metadata.name.full)
            player_stats.setdefault(column_names[5], []).append(player.player_stats.score)
            stas_soccer = player.player_stats.player_stats_soccer
            player_stats.setdefault(column_names[6], []).append(stas_soccer.duels_won)
            player_stats.setdefault(column_names[7], []).append(stas_soccer.duels_lost)
            player_stats.setdefault(column_names[8], []).append(stas_soccer.passes)
            player_stats.setdefault(column_names[9], []).append(stas_soccer.passes_completed)
            player_stats.setdefault(column_names[10], []).append(stas_soccer.stats_soccer_offensive.shots_total_inside_box)
            player_stats.setdefault(column_names[11], []).append(stas_soccer.stats_soccer_offensive.shots_total_outside_box)
            player_stats.setdefault(column_names[12], []).append(stas_soccer.stats_soccer_offensive.assists_total)
            player_stats.setdefault(column_names[13], []).append(stas_soccer.stats_soccer_offensive.offsides)
            player_stats.setdefault(column_names[14], []).append(stas_soccer.stats_soccer_foul.fouls_commited)
            player_stats.setdefault(column_names[15], []).append(stas_soccer.stats_soccer_foul.fouls_suffered)
    
    return DataFrame(player_stats, columns=column_names)


def team_statistics(fileName):
    xml = open(fileName).read()
    # print xml
    order = ts.CreateFromDocument(xml)
    column_names = ['id', 'team_name', 'alignament', 'period', 'score', 'duels_won', 'duels_lost',
                'passes_complited', 'passes_faild', 'shots_total', 'shots_on_goal', 'offsides', 
                'corner_kicks', 'corner_kicks_l', 'corner_kicks_r', 'freekicks', 'fouls_suffered',
                'fouls_commited', 'yelow-cards', 'red-cards', 'ball_possession', 'ball_possession_own_half',
                'ball_possession_opposing_half']
    team_stats = {}
    
    #per team
    for team in order.sports_event.team:    
        for period_stat in team.team_stats:
            stats = period_stat.team_stats_soccer
            team_stats.setdefault(column_names[0], []).append(team.team_metadata.id)
            team_stats.setdefault(column_names[1], []).append(team.team_metadata.name.full)
            team_stats.setdefault(column_names[2], []).append(team.team_metadata.alignment)
            team_stats.setdefault(column_names[3], []).append(period_stat.period_value)
            team_stats.setdefault(column_names[4], []).append(period_stat.score)
            team_stats.setdefault(column_names[5], []).append(stats.duels_won)
            team_stats.setdefault(column_names[6], []).append(stats.duels_lost)
            team_stats.setdefault(column_names[7], []).append(stats.passes_completed)
            team_stats.setdefault(column_names[8], []).append(stats.passes_failed)
            team_stats.setdefault(column_names[9], []).append(stats.stats_soccer_offensive.shots_total)
            team_stats.setdefault(column_names[10], []).append(stats.stats_soccer_offensive.shots_on_goal_total)
            team_stats.setdefault(column_names[11], []).append(stats.stats_soccer_offensive.offsides)
            team_stats.setdefault(column_names[12], []).append(stats.stats_soccer_offensive.corner_kicks)
            team_stats.setdefault(column_names[13], []).append(stats.stats_soccer_offensive.corner_kicks_left)
            team_stats.setdefault(column_names[14], []).append(stats.stats_soccer_offensive.corner_kicks_right)
            team_stats.setdefault(column_names[15], []).append(stats.stats_soccer_offensive.freekicks)
            team_stats.setdefault(column_names[16], []).append(stats.stats_soccer_foul.fouls_suffered)
            team_stats.setdefault(column_names[17], []).append(stats.stats_soccer_foul.fouls_committed)
            team_stats.setdefault(column_names[18], []).append(stats.stats_soccer_foul.yellow_cards)
            team_stats.setdefault(column_names[19], []).append(stats.stats_soccer_foul.red_cards)
        
            tracking = team.team_stats_tracking
            team_stats.setdefault(column_names[20], []).append(tracking.stats_ball.ballPossessionTime / tracking.stats_time.playedTime)
            team_stats.setdefault(column_names[21], []).append(tracking.stats_ball.ballPossessionTime_OwnHalf / tracking.stats_time.playedTime)
            team_stats.setdefault(column_names[22], []).append(tracking.stats_ball.ballPossessionTime_OpposingHalf / tracking.stats_time.playedTime)
    
    return DataFrame(team_stats, columns=column_names)

def extract_game_passes(fileName):
  
    DOMTree = minidom.parse(fileName)

    collection = DOMTree.documentElement
    
    action_events = collection.getElementsByTagName("action-soccer-other")
    column_names = ['id', 'period', 'minute', 'time_stamp', 'pass_type', 'team', 'player', 'second_player', 'x1', 'y1', 'x2', 'y2']
    passes_dic = {}
    for action in action_events:
        if action.getAttribute("action-type") == 'pass' and \
        action.getAttribute("pass-result") == 'completed' and \
        action.getAttribute("second-player-idref") != '':
            passes_dic.setdefault(column_names[0], []).append(action.getAttribute("id"))
            passes_dic.setdefault(column_names[4], []).append(action.getAttribute("pass-type"))
            passes_dic.setdefault(column_names[5], []).append(action.getAttribute("team-idref"))
            passes_dic.setdefault(column_names[6], []).append(action.getAttribute("player-idref"))
            passes_dic.setdefault(column_names[7], []).append(action.getAttribute("second-player-idref"))
            passes_dic.setdefault(column_names[1], []).append(action.getAttribute("period-value"))
            passes_dic.setdefault(column_names[2], []).append(action.getAttribute("minutes-elapsed"))
            passes_dic.setdefault(column_names[3], []).append(action.getAttribute("timestamp"))
            passes_dic.setdefault(column_names[8], []).append(action.getAttribute("x1"))
            passes_dic.setdefault(column_names[9], []).append(action.getAttribute("y1"))
            passes_dic.setdefault(column_names[10], []).append(action.getAttribute("x2"))
            passes_dic.setdefault(column_names[11], []).append(action.getAttribute("y2"))
    
    
    passes = DataFrame(passes_dic, columns=column_names, dtype = float)
    
    #set empty coordinates to 0
    passes.loc[[0, 138], [10, 11]] = 0
    
    #convert columns to appropriate data types
    passes['time_stamp'] = pd.to_datetime(passes.time_stamp)
    passes['id'] = passes['id'].astype(int)
    passes['period'] = passes['period'].astype(int)
    passes['minute'] = passes['minute'].astype(int)
    passes['x2'] = passes['x2'].astype(float)
    passes['y2'] = passes['y2'].astype(float)
    passes.sort(columns="time_stamp")
    
    #remove invalid data
    passes = passes[passes.x2 != 0]
    
    return passes

def __replace(original, replacement, list_):
    for i in range(len(list_)):
        if list_[i] == original:
            list_[i] = replacement
            
def __check_is_contained(element, list_):
    if element in list_:
        return True
    else:
        return False
    
def __convert(item):
    sub = ['A', 'B', 'C', 'D', 'E']
    counter = 0
    for i in range(len(item)):
        if not __check_is_contained(item[i], sub):
            __replace(item[i], sub[counter], item)
        counter += 1
    return "".join(item)

def __extract_ball_possessions(team_name, passes, time=5, check_distance = False):
    team = passes[passes.team == team_name]
    
    it = team.iterrows()
    
    index_previous, row_previous = next(it)
    
    ball_possessions = []
    ball_possession = []
    first = True
    for index, row in it:
        distance = np.sqrt(euclidean_distance_square(np.array([row_previous.x1, row_previous.y1]), np.array([row.x1, row.y1]))) 
        if check_distance == True and distance < 0.3:
            continue            
        if row_previous.second_player == row.player and (row.time_stamp - row_previous.time_stamp).total_seconds() < time:
            if first == True:
                ball_possession.append(row_previous.player)
                ball_possession.append(row_previous.second_player)
                first = False        
            ball_possession.append(row.second_player)
        else:
            if len(ball_possession) != 0:
                ball_possessions.append(ball_possession)
                ball_possession = []
            first = True
        index_previous = index
        row_previous = row        
    return ball_possessions
    
def __extract_motifs(ball_possessions, number_of_passes=3, convert_data=True):
    result = []
    for ball_posses in ball_possessions:
        if len(ball_posses) < number_of_passes+1:
            continue
        for i in range(len(ball_posses) - number_of_passes):
            if convert_data == True:
                result.append(__convert(ball_posses[i:i+number_of_passes+1]))
            else:
                result.append(ball_posses[i:i+number_of_passes+1])
    return result

def extract_game_motifs(teams_id, passes, time=5, check_distance = False, number_of_passes=3, convert_data=True):
    possessions_team1 = __extract_ball_possessions(teams_id[0], passes, time, check_distance)
    possessions_team2 = __extract_ball_possessions(teams_id[1], passes, time, check_distance)
    
    motifs_team1 = __extract_motifs(possessions_team1, number_of_passes, convert_data)
    motifs_team2 = __extract_motifs(possessions_team2, number_of_passes, convert_data) 
    return motifs_team1, motifs_team2


def __extract_double_pass_team(team_id, column_names1, players_dic, players, passes):
    passess_tmp = DataFrame(__extract_motifs(__extract_ball_possessions(team_id, passes, check_distance=True), 2, False))
    players = DataFrame(players_dic, columns=column_names1)
    double_passes = passess_tmp[passess_tmp[0] == passess_tmp[2]]
    dd = Series()
    dd = dd.append(double_passes[0])
    dd = dd.append(double_passes[1])
    ttt = DataFrame(dd, columns=['id'])
    result = pd.merge(ttt, players, left_on='id', right_on='id')['name']
    return result.value_counts()

def extract_double_passes(fileName, team_id):
    passes = extract_game_passes(fileName)
    DOMTree = minidom.parse(fileName)
    collection = DOMTree.documentElement
    column_names1 = ['id', 'jersy', 'name']
    players_dic = {}
    players = collection.getElementsByTagName("player-metadata")
    for player in players:
        name = player.getElementsByTagName('name')[0]
        players_dic.setdefault(column_names1[0], []).append(player.getAttribute('id'))
        players_dic.setdefault(column_names1[1], []).append(player.getAttribute('uniform-number'))
        players_dic.setdefault(column_names1[2], []).append(name.getAttribute('full'))
    
    result_team1 = __extract_double_pass_team(team_id[0], column_names1, players_dic, players, passes)
    result_team2 = __extract_double_pass_team(team_id[1], column_names1, players_dic, players, passes)
    
    return result_team1, result_team2