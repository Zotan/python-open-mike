---
title: "Python 'open mike' events at IRF"
layout: default
---

![IRF logo](/IRF.jpg)

RSS Feed for future events: <a href="/python-open-mike/feed.xml"><img style="height: 1rem;" alt="[RSS feed]" src="/python-open-mike/rss.svg"></a>

# Format

Eventually it could be a platform where participants show something useful to
others and have creative discussions about programing. But to warm up and get 
into the mood of hacking each event will have a theme and we will suggest 
exercises. Participants can prepare these exercises but do not have to. 
We go through the exercise and solutions together but those who have solved 
the exercises can present alternative solutions which we discuss together.

At each event we fix the dates for the next event and together we choose a
theme.


# What to expect

- Informal events.
- Interaction.
- Questions, answers, and discussions.

The goal is to discuss, ask questions, and to demo.

# What not to expect

Do not expect a semester-long course or lecture series where you can sit back
and somebody presents some slides. There are no slides, and there is no
lecture.


## Exercises

You can email solutions to Daniel Kastinen (daniel.kastinen@irf.se) who will
collect them and make them available (without names) so that you can
compare. It is OK to prepare all or prepare none.


## Next event


<ul>
  {% for post in site.posts %}
    {% if post.status != 'past' %}
      <li>
        <a href="{{ post.url | prepend:site.baseurl }}">{{ post.title }} ({{ post.time }}, room: {{ post.room }})</a>
      </li>
    {% endif %}
  {% endfor %}
</ul>


## Past events

<ul>
  {% for post in site.posts %}
    {% if post.status == 'past' %}
      <li>
        <a href="{{ post.url | prepend:site.baseurl }}">{{ post.title }}</a>
      </li>
    {% endif %}
  {% endfor %}
</ul>


## Recommended reading

- [Real Python Tutorials](https://realpython.com)
- [The Hitchhiker’s Guide to Python!](https://docs.python-guide.org)
- [Python 3 Module of the Week](https://pymotw.com/3/)
- [Daily Programmer reddit](https://www.reddit.com/r/dailyprogrammer)


## Topics ideas for future events

 - Context managers
 - TCP/IP
 - Functional programming
 - `collections`
 - File I/O
 - `pandas`
 - `itertools`
 - decorators
 - The how and why of web applications
 - `tornado` vs `bottle` web framework
 - data streaming in Python?
 - utilisation of multiple CPUs (e.g. mpi4py-fft)
 - when to yield
 - @classmethod, @staticmethod and other OOP topics
 - Serialization of python objects in human readable format (json, yaml, csv)
 - Configuring the behaviour of your program
 - How to use argparse

