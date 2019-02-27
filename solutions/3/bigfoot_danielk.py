import os
import glob
import shutil
import pandas as pd

cwd = os.path.abspath('.')
cwd_split = cwd.split(os.sep)
dist_name = 'python-open-mike'
if not dist_name in cwd_split:
    data_folder = 'big_data' + os.sep
else:
    data_folder = cwd_split[:(cwd_split.index(dist_name)+1)]
    data_folder += ['data', 'big_data']
    data_folder = os.sep + os.path.join(*data_folder)

csv_files = glob.glob(data_folder + os.sep + '**' + os.sep +'*.csv', recursive=True)
txt_files = glob.glob(data_folder + os.sep + '**' + os.sep +'*.txt', recursive=True)

#make sure we dont list wow dir if it exists
txt_files = [txt for txt in txt_files if txt.split(os.sep)[-2] != 'wow']

states = glob.glob(data_folder + os.sep + '*' + os.sep)

states = [state.split(os.sep)[-2] for state in states]

print('States found:')
print(', '.join(states) + '\n'*2)

if 'comments' in states:
    del states[states.index('comments')]

kw = {
    'delimiter': ',',
    'encoding': 'UTF-8',
    'header': 0,
    'decimal': '.',
}

state_sightings = [None]*len(csv_files)
for csv_ind, csv_file in enumerate(csv_files):
    df_new = pd.read_csv(csv_file, **kw)

    if csv_ind > 0:
        df.append(df_new)
    else:
        df = df_new

    state_sightings[csv_ind] = ( csv_file.split(os.sep)[-2], df_new.shape[0] )

state_sightings.sort(key=lambda x: x[1])

for state, cnt in state_sightings:
    print(f'{state:20s}: {cnt:4d} sightings')

wow_dir = data_folder + os.sep + 'wow'

if os.path.exists(wow_dir):
    wow_list = glob.glob(wow_dir + os.sep + '*')
    print(f'{wow_dir} exists, deleting contents: {len(wow_list)} items')
    for wow_stuff in wow_list:
        os.remove(wow_stuff)
else:
    os.mkdir(wow_dir)

for txt_file in txt_files:
    with open(txt_file, 'r') as f:
        sighting = f.readline()

        if 'howl' in sighting.split(' '):
            print(f'Howl detected in {txt_file} (moving to wow dir), report {len(sighting)} characters long.')
            shutil.copy2(txt_file, wow_dir + os.sep + txt_file.split(os.sep)[-1])

