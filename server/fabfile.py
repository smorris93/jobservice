from fabric.api import env, run
from fabric.operations import run
import os

env.hosts = ['pc1.leela', 'pc2.leela', 'pc3.leela', 'pc4.leela', 'pc5.leela', 'pc6.leela', 'pc8.leela', 'pc9.leela', 'pc10.leela''pc11.leela', 'pc12.leela', 'pc13.leela', 'pc14.leela', 'pc15.leela', 'pc17.leela', 'pc18.leela', 'pc19.leela', 'pc20.leela']

x = env.hosts
env.password = 'password'
HOME_PATH = '/home/is120008/Documents/'

def virtualenv(command):
    # Runs the given command in a virtual environment
    env = home_path
    source = 'source %s/jobservice/bin/activate && ' % env
    run(source + command)


def run_client():
    # Run the client on each of the env.hosts
    for y in x:
        virtualenv('python %s/jobservice/client/truecrack.py' % HOME_PATH)
  
