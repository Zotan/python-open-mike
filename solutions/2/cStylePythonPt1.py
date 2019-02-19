import csv

kommunCsv    = open('2019-02-12-skattesats-2-kommun.csv', newline='')
landstingCsv = open('2019-02-12-skattesats-1-landsting.csv', newline='')
outputCsv    = open('output.csv', "w", newline='')

# Skip headers
kommunHeader = kommunCsv.readline().rstrip('\n').split(',')
landstingHeader = landstingCsv.readline().rstrip('\n').split(';')[1:]

kommunList = []
landstingList = []

kommunReader = csv.reader(kommunCsv)
for row in kommunReader:
    kommunList.append(row)

landstingReader = csv.reader(landstingCsv, delimiter=';')
for row in landstingReader:
    landstingList.append(row)

outputWriter = csv.writer(outputCsv)

# Prep the header
outputWriter.writerow(kommunHeader + landstingHeader)

# Sort the lists
kommunList.sort(key=lambda x: x[0].split()[0])
landstingList.sort(key=lambda x: x[0].split()[0])

kIter = iter(kommunList)
lIter = iter(landstingList)

for index in range(len(kommunList)):
    outputWriter.writerow(kommunList[index] + landstingList[index][1:])

landstingCsv.close()
kommunCsv.close()
outputCsv.close()
