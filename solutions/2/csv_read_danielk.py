#!/usr/bin/env python

import pandas as pd

files = []

default_opts = {
    'delimiter': ',',
    'encoding': 'UTF-8',
    'header': 0,
    'decimal': '.',
    'index_col': 0,
}

root = '../../data/'

opts = default_opts.copy()
opts['delimiter'] = ';'
opts['decimal'] = ','
files.append((
    '2019-02-12-skattesats-1-landsting.csv', 
    opts.copy(),
))

opts = default_opts.copy()
opts['encoding'] = 'ISO-8859-1'
files.append((
    '2019-02-12-skattesats-2-kommun.csv', 
    opts.copy(),
))

#Besides setup of settings: 5 lines of code

data = []

for fname, kw in files:
    df = pd.read_csv(root + fname, **kw)
    data.append(df)

final_data_v1 = pd.concat(data, sort=True)
final_data_v2 = pd.merge(data[0], data[1], left_index=True, right_index=True)

print(final_data_v1)
print(final_data_v2)



#for index, row in final_data_v1.iterrows():
#    print(row)

#for index, row in final_data_v2.iterrows():
#    print(row)


#check if they actually overlap at all
#_regions = []
#for df in data:
#    print(df.index.values)
#    _regions += df.index.values.tolist()
#print('any overlap? ', len(_regions) != len(set(_regions)))