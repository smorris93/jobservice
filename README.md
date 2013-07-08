jobservice
==========

You want to make your computers work for you? Good. 

Installation
------------

As root (Debian):

        # aptitude install python-virtualenv libevent-dev libpython-dev

As root (Ubuntu):

        # aptitude install python-virtualenv libevent-dev python-dev

As unprivileged user:

        $ virtualenv <dest-dir>
        $ cp -R <repos-dir>/server <dest-dir>
        $ cp -R <repos-dir>/client <dest-dir>
        $ cd <dest-dir>
        $ source bin/activate
        $ pip install Flask-RESTful
        $ pip install requests
        $ pip install gevent-socketio

Usage
-----

        $ python server/controller.py <number of ranges> <timeout per range>
        $ python client/client.py
