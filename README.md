jobservice
==========

Installation
------------

        $ aptitude install python-virtualenv libevent-dev
        $ virtualenv /tmp/example
        $ cp *.py /tmp/example
        $ cd /tmp/example
        $ source bin/activate
        $ pip install Flask-RESTful
        $ pip install requests
        $ pip install gevent-socketio

Usage
-----

        $ python controller.py <number of ranges> <timeout per range>
        $ python client.py <success> <rangeId>
