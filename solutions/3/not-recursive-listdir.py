#!/usr/bin/env python3

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


def main(basepath):
    output = basepath / "wow"

    os.makedirs(output, exist_ok=True)
    clear_directory(output)

    for path in find_howls(basepath):
        targetfn = output.joinpath(path.parent.name + '-' + path.name)
        targetfn.write_text(path.read_text())


if __name__ == '__main__':
    main(Path(os.path.abspath(os.path.expanduser(sys.argv[1]))))
