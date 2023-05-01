import pandas as pd
MODULE_NAME = 'pandas'

PATH_KEY = 'path'
DATA_KEY = 'data'
COL_KEY = 'col'

def open_csv(**kwargs):
    return pd.read_csv(kwargs[PATH_KEY])

def groupby(**kwargs):
    return kwargs[DATA_KEY].groupby(kwargs[COL_KEY])

def lines(**kwargs):
    return kwargs[DATA_KEY].shape[0]