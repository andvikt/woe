import os
import numpy as np
import woe.feature_process as fp
import woe.GridSearch as gs
import pandas as pd
from sklearn.model_selection import train_test_split as tts

def process(data_in
            , config_features = 'config'):
    '''
    process data_in CSV with woe transformations
    :config_features = 'config.csv'
    :data_in 
    :data_out
    :config_woe=None
    :return: None
    '''

    config_path = os.getcwd()+'/' + config_features + '.csv'
    data_path = os.getcwd()+'/' + data_in + '.csv'
    feature_detail_path = os.getcwd()+'/' + data_in + '_stats_wide' + '.csv'
    rst_pkl_path = os.getcwd()+'/woe_rule.pkl'
    # train woe rule
    feature_detail,rst = fp.process_train_woe(infile_path=data_path
                                            ,outfile_path=feature_detail_path
                                            ,rst_path=rst_pkl_path
                                            ,config_path=config_path)
    
    # proc woe transformation
    woe_train_path = os.getcwd()+'/' + data_in + '_out' + '.csv'
    fp.process_woe_trans(data_path,rst_pkl_path,woe_train_path,config_path)

    #make short statistics in excel
    stats = (feature_detail.groupby('var_name').agg({'iv': max})
            .sort_values(['iv'], ascending=False)
        )
    writer = pd.ExcelWriter(data_in + '_stats.xlsx')
    stats.to_excel(writer,'Short')
    feature_detail.to_excel(writer,'Full')
    writer.save()

    return feature_detail
