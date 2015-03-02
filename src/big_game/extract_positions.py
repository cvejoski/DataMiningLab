'''
Created on Jan 22, 2015

@author: kostadin
'''

import pandas as pd
from pandas import   MultiIndex

def extract(file_path="../Resources/BigGame/Data/130375.pos"):
    frames = ['Frames'] * 3
    team1 = ['Team1'] * 44
    team2 = ['Team2'] * 44
    referees = ['Referees'] * 9
    ball = ['Ball'] * 6
    additionalInfo = ['AdditionalInfo'] * 4
    
    id_ = []
    for i in range(22):
        id_ += ['ID'+str(i)] * 4   
    
    for i in range(22, 25):
        id_ += ['ID'+str(i)] * 3  
    
    frames_data = ['FrameNumber', 'Minute', 'Section']    
    players_data = ['Jersy','X', 'Y', 'Speed'] * 22
    referees_data = ['X', 'Y', 'Speed'] * 3
    ball_data = ['X', 'Y', 'Z', 'Speed', 'Flag', 'Possession']
    addInfo_data = ['A', 'B', 'C', 'D']
    
    level_0 = frames + team1 + team2 + referees + ball + additionalInfo
    level_1 = ['Data'] * 3 + id_ + ['Data'] * 10
    level_2 = frames_data + players_data + referees_data + ball_data + addInfo_data
    
    column_names = MultiIndex.from_arrays([level_0, level_1, level_2])
    
    tmp_data = pd.read_csv(file_path, delimiter='[^0-9.-]*', 
                     header=None, names=column_names, encoding='utf-8')
    data = tmp_data.set_index([tmp_data.Frames.Data.Section, tmp_data.Frames.Data.Minute, tmp_data.Frames.Data.FrameNumber])
    del tmp_data
    del data['Frames']
    del data['AdditionalInfo']['Data']['D']
    return data