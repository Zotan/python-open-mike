---
layout: post
title: "2019-03-19: Filesystem"
time: "14:30"
room: "Aniara"
author: "the organizers"
status: "past"
---


# Agenda

Interacting with the file-system trough Python. Creating and deleting files and folders. Finding and opening files.


# Problems

In [the data folder](https://github.com/danielk333/python-open-mike/tree/gh-pages/data) there is a folder structure that looks like:

.. code-block::

    big_data/
    |--conf.py
    |--comments/
    |  |--stuff.txt
    |--Alabama/
    |  |--reports.csv
    |  |--0.txt
    |  |--1.txt
    |  |-- ...
    |--Alaska/
    |  |--reports.csv
    |  |--0.txt
    |  |--1.txt
    |  |-- ...
    |-- ...

The data is Bigfoot sightings in USA, downloaded with [bfro-download](https://github.com/timothyrenner/bfro_sightings_data). It is ordered according to state, each containing a reports.csv with the actual data.

The **conf.py** contains parameters useful for interpreting the data.

The **.txt** files contain one sighting report each (1 line).

## The task is to:

1. Create a list of all states there is data for.
2. Create a folder called **wow** in the **big_data/** folder. If the directory exists, make sure it is empty.
3. *Copy* (do not move) all **.txt** files that contains the word "howl" to the **big_data/wow** folder.

## Optional cool stuff:

4. Use the csv-reading from last event to read all different states data.
5. Sort states according to number of sightings, what is the most "Bigfoot" state in USA?

## Hints:

1. [Python os](https://docs.python.org/3/library/os.html)
2. [Python glob](https://docs.python.org/3.7/library/glob.html)
