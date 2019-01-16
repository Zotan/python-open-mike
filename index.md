---
title: "Python 'open mike' events at IRF"
layout: default
---

![IRF logo](/IRF.jpg)

RSS Feed for future events: <a href="/python-open-mike/feed.xml"><img style="height: 1rem;" alt="[RSS feed]" src="data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyB3aWR0aD0iN21tIiBoZWlnaHQ9IjdtbSIgdmVyc2lvbj0iMS4xIiB2aWV3Qm94PSIwIDAgNyA3IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDAsLTI5MCkiPjxwYXRoIGQ9Im0wLjc4MTY3IDI5MGg1LjQzNjdxMC4zMjY2NyAwIDAuNTQ4MzMgMC4yMzMzMyAwLjIzMzMzIDAuMjIxNjcgMC4yMzMzMyAwLjU0ODMzdjUuNDM2N3EwIDAuMzI2NjctMC4yMzMzMyAwLjU2LTAuMjIxNjcgMC4yMjE2Ny0wLjU0ODMzIDAuMjIxNjdoLTUuNDM2N3EtMC4zMjY2NyAwLTAuNTYtMC4yMjE2Ny0wLjIyMTY3LTAuMjMzMzMtMC4yMjE2Ny0wLjU2di01LjQzNjdxMC0wLjMyNjY2IDAuMjIxNjctMC41NDgzMyAwLjIzMzMzLTAuMjMzMzMgMC41Ni0wLjIzMzMzem0wLjk2ODMzIDQuNjY2N3EtMC4yNTY2NyAwLTAuNDIgMC4xNjMzNC0wLjE2MzMzIDAuMTYzMzMtMC4xNjMzMyAwLjQyIDAgMC4yNTY2NiAwLjE2MzMzIDAuNDIgMC4xNjMzMyAwLjE2MzMzIDAuNDIgMC4xNjMzMyAwLjI1NjY3IDAgMC40Mi0wLjE2MzMzIDAuMTYzMzMtMC4xNjMzNCAwLjE2MzMzLTAuNDIgMC0wLjI1NjY3LTAuMTc1LTAuNDItMC4xNjMzMy0wLjE2MzM0LTAuNDA4MzMtMC4xNjMzNHptLTAuNTgzMzMtMS45NDgzdjAuNzgxNjdxMC45OCAwLjAyMzMgMS42NDUgMC42ODgzMyAwLjY2NSAwLjY2NSAwLjY4ODMzIDEuNjQ1aDAuNzgxNjdxLTAuMDM1LTEuMzMtMC45MS0yLjIwNS0wLjg3NS0wLjg3NS0yLjIwNS0wLjkxem0wLTEuNTUxN3YwLjc4MTY3cTEuNjU2NyAwLjAzNSAyLjc1MzMgMS4xMzE3IDEuMDk2NyAxLjA5NjcgMS4xMzE3IDIuNzUzM2gwLjc4MTY3cS0wLjA1ODMzMy0xLjk4MzMtMS4zNzY3LTMuMjktMS4zMDY3LTEuMzE4My0zLjI5LTEuMzc2N3oiLz48L2c+PC9zdmc+Cg=="></a>

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

