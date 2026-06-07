import pandas as pd

from utils.Machine_learning_Backend_codes.Feature_matrix_gen import run as ml_run1
from utils.Machine_learning_Backend_codes.RFC_output_generation import run2 as ml_run2
from utils.Deep_learning_Backend_codes.Data_encoding import run as dl_run1
from utils.Deep_learning_Backend_codes.FNN_output_generation import run2 as dl_run2

def user_input_handling(SgRNA, target_DNA, model):
    a = SgRNA
    b = target_DNA
    heading = {'sgRNA':[],'Target':[],'Result':[],'Position':[]}
    df = pd.DataFrame(heading)
    row = 0
    print(a, b)
    for i in range(len(b)-len(a)+1):
        target = b[i:len(a) + i]
        df.at[row, 'sgRNA'] = a 
        df.at[row, 'Target'] = target
        min_ind = i + 1
        max_ind = len(a) + i
        position = "[" + str(min_ind) + "-" + str(max_ind) + "]"
        df.at[row, 'Position'] = position
        row += 1
    df.to_excel('utils/input_data.xlsx', index=False)
    df.to_csv('utils/input_data.csv', index=False)

    if model == 'Machine Learning':
        ml_run1()
        ml_run2()
    elif model == 'Deep Learning':
        dl_run1()
        dl_run2()
