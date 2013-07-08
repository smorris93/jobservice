import sys

from gevent import monkey
from socketio import socketio_manage
from socketio.server import SocketIOServer
from werkzeug.wsgi import SharedDataMiddleware

from flask import Flask, request, render_template
from flask.ext.restful import Api

from rangemanager import RangeManager
from resources import FetchJob, Report, Progress, Reset
from namespaces import PushNamespace


def main():
    try:
        # init
        lModel = RangeManager(int(sys.argv[1]), int(sys.argv[2]))

        monkey.patch_all()
        lApp = Flask(__name__)
        lApp.debug = True
        lApi = Api(lApp)
        FetchJob.sModel = lModel
        Report.sModel = lModel
        Progress.sModel = lModel
        Reset.sModel = lModel
        PushNamespace.sModel = lModel

        # routes
        lApp.add_url_rule('/',                      'poll', poll)
        lApp.add_url_rule('/socket.io/<path:path>', 'socket.io', run_socketio)
        lApi.add_resource(FetchJob,                 '/fetch')
        lApi.add_resource(Report,                   '/report')
        lApi.add_resource(Progress,                 '/progress')
        lApi.add_resource(Reset,                    '/reset')

        # go
        lApp = SharedDataMiddleware(lApp, {})
        lServer = SocketIOServer(
            ('0.0.0.0', 5000),
            lApp,
            resource="socket.io",
            policy_server=False)
        lServer.serve_forever()
    except IndexError:
        print "Usage: " + sys.argv[0] + \
            " <number of ranges> <timeout per range>"


def poll():
    return render_template('progress.html')


def run_socketio(path):
    socketio_manage(request.environ, {'': PushNamespace}, path)
    # workaround to omit the "ValueError: View function did not
    #     return a response" exception
    return render_template('dummy.html')


if __name__ == '__main__':
    main()
