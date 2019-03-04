#!/usr/bin/env python3

import csv
import os
import re
import sys

from pathlib import Path


def collect_subfolders(path):
    """Return a list of all subfolder of 'path'

    This includes path itself as the first element of the list.
    The elements in the list are ordered in depth, i.e. elements
    are guaranteed to not be lower in the hierarchy than any other
    element in the list with a lower index number."""
    pathqueue = [path]
    paths = []

    while len(pathqueue) > 0:
        path = pathqueue.pop(0)

        if not path.is_dir():
            continue

        paths.append(path)
        pathqueue += [entry for entry in path.iterdir() if entry.is_dir()]

    return paths


def collect_files(basepath, ext='txt'):
    result = []

    for path in collect_subfolders(basepath):
        result += [entry for entry in path.iterdir()
                   if entry.is_file() and entry.suffix == os.extsep + ext]

    return result


def clear_directory(path):
    paths_to_delete = collect_subfolders(path)

    while len(paths_to_delete) > 0:
        path = paths_to_delete.pop()

        for entry in [e for e in path.iterdir()]:
            if entry.is_dir():
                entry.rmdir()
            else:
                entry.unlink()


def find_howls(basepath):
    howl_pattern = re.compile(r'[^a-z]howl(ing|ed|s)?[^a-z]', re.IGNORECASE)

    matches = []

    for path in collect_files(basepath):
        content = path.read_text()
        if howl_pattern.search(content) is not None:
            matches.append(path)

    print('There where {} howls.'.format(len(matches)))

    return matches


def detailed_observations(basepath):
    observations = {}
    classifications = set()

    for path in collect_files(basepath, ext='csv'):
        with open(path, 'r', encoding='utf-8', newline='') as fd:
            reader = csv.reader(fd)

            for idx, line in enumerate(reader):
                if idx == 0:
                    continue

                _, fileidx, _, county, state, _, lat, lon, date, number, classification, geohash = line

                if state not in observations:
                    observations[state] = {}
                if classification.startswith('Class '):
                    classification = classification[-1:]
                if classification not in observations[state]:
                    observations[state][classification] = 0
                classifications.add(classification)
                observations[state][classification] += 1

    sorted_by_obs = [state for state in observations.keys()]
    sorted_by_obs.sort(key=lambda e: sum([amount for amount in observations[e].values()]), reverse=True)
    print('States with the most observations:',
          ', '.join(sorted_by_obs[:3]))

    for classification in sorted(classifications):
        sorted_by_class = [state for state in observations.keys()]
        sorted_by_class.sort(key=lambda e: observations[e].get(classification, 0), reverse=True)
        print('States with the most class {} observations:'.format(classification),
              ', '.join(sorted_by_class[:3]))


def main(basepath):
    output = basepath / "wow"

    os.makedirs(output, exist_ok=True)
    clear_directory(output)

    for path in find_howls(basepath):
        targetfn = output.joinpath(path.parent.name + '-' + path.name)
        targetfn.write_text(path.read_text())

    detailed_observations(basepath)


if __name__ == '__main__':
    main(Path(os.path.abspath(os.path.expanduser(sys.argv[1]))))
