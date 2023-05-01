import os

col_name = 'review/score'

def get_flat_names(file_path, ext=None):
    file_list = []
    for item in os.listdir(file_path):
        if not os.path.isfile(os.path.join(file_path, item)):
            continue
        if not ext or ext == 'all' or os.path.splitext(item)[1] != ext:
            continue
        file_list.append(os.path.join(file_path, item))
    return file_list

def get_datasets_defualt():
    real_path = os.path.realpath(os.path.dirname(__file__))
    real_path = os.path.join(real_path, 'files', 'sliced')
    return get_flat_names(real_path, '.csv')