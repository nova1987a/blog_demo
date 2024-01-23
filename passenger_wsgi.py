#import imp
#import os
#import sys
import sys, os, re, imp, threading, signal, traceback, socket, select, struct, logging, errno
import djdemo.wsgi


sys.path.insert(0, os.path.dirname(__file__))

wsgi = imp.load_source('wsgi', 'manage.py')
application = djdemo.wsgi.application
