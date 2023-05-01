import os
import time
import resource 

import drawer
import data_model

import shells.polars_shell as pl
import shells.pandas_shell as pd


def count_metrics(samples, to_print=True):
    mean_val = sum(samples) / len(samples)
    div = 0
    st_div = 0
    for i in samples:
        div += i - mean_val
        st_div += (i - mean_val) ** 2
    div /= len(samples)
    st_div /= len(samples)
    st_div **= 0.5
    if to_print:
        print('Mean value: {a}'.format(a=mean_val))
        print('Diviation: {a}'.format(a=div))
        print('Standard Diviation: {a}'.format(a=st_div))
    return mean_val, div, st_div

def run_single(test_function, **kwargs):  # abstract function for a single check
    time_start = time.perf_counter()
    test_function(**kwargs)
    time_elapsed = (time.perf_counter() - time_start)
    memMb=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024.0/1024.0
    return time_elapsed, memMb 

def run_many(n, test_function, **kwargs):  # abstract function for n checks and aggregation
    secs = [0] * n
    memo = [0] * n
    for i in range(n):
        secs[i], memo[i] = run_single(test_function, **kwargs)
    t_m, t_d, t_sd = count_metrics(secs, to_print=False)
    m_m, m_d, m_sd = count_metrics(memo, to_print=False)
    return {
        'time': {
            'mean': t_m,
            'diviation': t_d,
            'standard diviation': t_sd,
        },
        'memory': {
            'mean': m_m,
            'diviation': m_d,
            'standard diviation': m_sd,
        },
    }


def run_all():
    modules = [pl, pd]  # set modules for checking
    n = 30  # set number of repeats for getting stochastically better results
    data_sets = data_model.get_datasets_defualt()  # read our data
    result = {}  # an empty result
    for m in modules:  # let us iterate choosen modules
        result[m.MODULE_NAME] = {}   # an empty result for a single module
        # print(m.MODULE_NAME)
        for d in data_sets:
            filename = os.path.basename(d)
            result[m.MODULE_NAME][filename] = {}
            # print(filename)

            kw = {'path': d}  # set dict for kwargs
            open_res = run_many(n, m.open_csv, **kw)  # check the open function
            result[m.MODULE_NAME][filename]['open'] = open_res  # save open res

            data = m.open_csv(**kw)  # and now let us read data properly, please
            kw = {'data': data}  # set dict with data for kwargs
            result[m.MODULE_NAME][filename]['lines'] = m.lines(**kw)  # save len of data

            kw['col'] = data_model.col_name
            gr_res = run_many(n, m.groupby, **kw)  # check the groupby function
            result[m.MODULE_NAME][filename]['groupby'] = gr_res  # save groupby res
    return result


if __name__ == '__main__':
    res = run_all()
    # print(res)
    drawer.print_res(res)

