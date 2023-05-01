import os
import math
import pandas as pd

def read_default_books():
    real_path = os.path.realpath(os.path.dirname(__file__))
    df = pd.read_csv(os.path.join(real_path, '..', 'files', 'Books_rating.csv'))
    return df

def get_default_save_path():
    real_path = os.path.realpath(os.path.dirname(__file__))
    return os.path.join(real_path, '..', 'files', 'sliced')

def save_slice(df, n, dir_path):
    file_name = 'books_' + str(n) + '.csv'
    df.to_csv(os.path.join(dir_path, file_name))

def made_slices(df, n, max_val, min_val, dir_path=None):
    if dir_path == None:
        dir_path = get_default_save_path()
    df = df.iloc[:max_val]
    k = math.floor((max_val - min_val) / n)
    for i in range(n + 1):
        amount = max_val - k * i
        if amount <= 0:
            continue
        save_slice(df.iloc[:(amount)], amount, dir_path)

if __name__ == '__main__':
    df = read_default_books()
    made_slices(df, 5, 6000, 3000)
