---
layout: post
title: "2019-03-19: Filesystem"
time: "14:30"
room: "Aniara"
author: "the organizers"
status: "next"
---


# Agenda

Interacting with the file-system trough Python. Creating and deleting files and folders, finding files.


# Problems

In [the data folder](https://github.com/danielk333/python-open-mike/tree/gh-pages/data) there is a folder structure that looks like:

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

## The task is to:

1. Store the full **data_folder** path in a variable without explicitly writing it in the code.
2. Create a list of all **reports.csv** file paths (full paths)
3. Create a list of all states there is data for (just state names, no slashes or paths)
4. Import the *classes* variable from **conf.py** into the script
5. List all files in the **comments** folder.

## Optional task:

5. Use the csv-reading from last event to read all different states data
6. Merge the data into a single table
7. Find the most "Bigfoot" state in USA