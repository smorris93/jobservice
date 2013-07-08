jobservice
==========

You want to make your computers work for you? Good. 

Installation
------------

As root:

        # aptitude install python-virtualenv libevent-dev

As unprivileged user:

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