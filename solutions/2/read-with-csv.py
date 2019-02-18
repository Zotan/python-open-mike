#!/usr/bin/env python

import csv


if __name__ == '__main__':
    regions = {}
    header = []

    datafiles = [('data/2019-02-12-skattesats-1-landsting.csv', 'utf-8', ';'),
                 ('data/2019-02-12-skattesats-2-kommun.csv', 'windows-1252', ',')]

    for fn, encoding, delimiter in datafiles:
        with open(fn, 'r', encoding=encoding) as fd:
            reader = csv.reader(fd, delimiter=delimiter)

            for nr, row in enumerate(reader):
                if nr == 0:
                    header += row[1:]
                    continue
                region = row[0]
                data = [float(value.replace(',', '.')) for value in row[1:]]
                if region not in regions:
                    regions[region] = []
                regions[region] += data

    print(regions)

