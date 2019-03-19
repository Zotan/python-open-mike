import os
import glob
import shutil

dirList = glob.glob('data' + os.sep + 'big_data' + os.sep + '*')
stateCount = {}
wowDirName = 'data' + os.sep + 'big_data' + os.sep + 'wow'

if not os.path.exists(wowDirName):
    os.mkdir(wowDirName)
else:
    # There's something there, but what?
    if os.path.isfile(wowDirName):
        print('File found at wow location')
        exit()
    else:
        # Should be a directory
        shutil.rmtree(wowDirName)
        os.mkdir(wowDirName)

for directory in dirList:
    if os.path.isdir(directory) and \
       (directory.split(os.sep)[-1] != 'comments') and \
       (directory.split(os.sep)[-1] != 'wow'):
        stateName = directory.split(os.sep)[-1]
        stateCount[stateName] = 0
        dataFileList = glob.glob(directory + os.sep + '*.txt')
        for dataFile in dataFileList:
            stateCount[stateName] += 1
            with open(dataFile) as howlFile:
                for line in howlFile:
                    if 'howl' in line:
                        filename = dataFile.split(os.sep)[-1]
                        stateName = dataFile.split(os.sep)[-2]
                        newFileName = str(stateName) + '-Howl-' + str(filename)
                        shutil.copy(dataFile, wowDirName + os.sep + newFileName)
                        break

sortedStates = sorted((value, key) for (key, value) in stateCount.items())
print('State with the most records is: ' +
      sortedStates[-1][1] +
      ', ' +
      str(sortedStates[-1][0]))
