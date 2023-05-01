from uniplot import plot


def collect_ticks(result, key, *args):
    sup_dict = {}
    for filename, results in result[key].items():
        l = int(filename.split('_')[1].split('.')[0])
        sup_dict[l] = results[args[0]][args[1]][args[2]]
    sup_keys = list(sup_dict.keys())
    sup_keys.sort()
    sup_ticks = []
    for sup in sup_keys:
        sup_ticks.append(sup_dict[sup])
    return sup_ticks


def print_res(result):
    key_rest = ['open', 'time', 'mean']
    # key_rest = ['open', 'time', 'diviation']
    # key_rest = ['open', 'time', 'standard diviation']
    # key_rest = ['open', 'memory', 'mean']
    # key_rest = ['open', 'memory', 'diviation']
    # key_rest = ['open', 'memory', 'standard diviation']
    # key_rest = ['groupby', 'time', 'mean']
    # key_rest = ['groupby', 'time', 'diviation']
    # key_rest = ['groupby', 'time', 'standard diviation']
    # key_rest = ['groupby', 'memory', 'mean']
    # key_rest = ['groupby', 'memory', 'diviation']
    # key_rest = ['groupby', 'memory', 'standard diviation']
    sup_ticks_pd = collect_ticks(result, 'pandas', *key_rest)
    sup_ticks_pl = collect_ticks(result, 'polars', *key_rest)

    plot([sup_ticks_pd, sup_ticks_pl],
         legend_labels = ['pandas', 'polars'],
         lines = True)

if __name__ == '__main__':
    import mock
    result = mock.get_default_dict()
    print_res(result)
