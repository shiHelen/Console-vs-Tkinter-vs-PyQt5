import polars as pl
MODULE_NAME = 'polars'

PATH_KEY = 'path'
DATA_KEY = 'data'
COL_KEY = 'col'

def open_csv(**kwargs):
    return pl.read_csv(kwargs[PATH_KEY])

def groupby(**kwargs):
    return kwargs[DATA_KEY].groupby(kwargs[COL_KEY])

def lines(**kwargs):
    return kwargs[DATA_KEY].shape[0]