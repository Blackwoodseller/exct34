#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
dirlogger - Utility to monitor directory specified events.
(create, modify, move, delete directory or file)

    python dirlogger.py directory_path log_file_name | --help

"""
import sys
import os.path
import logging
import time
import getopt

from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler


class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg


def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "h", ["help"])
        except getopt.error, msg:
            raise Usage(msg)
    except Usage, err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, "for help use --help"
        return 2
    for o, a in opts:
        if o in ("-h", "--help"):
            print __doc__
            sys.exit(0)

    if len(args) != 2:
        print __doc__
        sys.exit(0)

    dir_name = args[0]
    log_file_name = args[1]

    if not os.path.isdir(dir_name):
        print dir_name + " is not valid directory name."
        sys.exit(2)

    try:
        with open(name=log_file_name, mode='w') as f:
            pass
    except:
        print log_file_name + " is not valid path."
        sys.exit(2)

    logging.basicConfig(format = u'[%(asctime)s] %(message)s', level=logging.INFO, filename=log_file_name)
    observer = Observer()
    observer.schedule(LoggingEventHandler(), path=dir_name, recursive=True)
    observer.start()

    try:
        while True:
                time.sleep(0.1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == '__main__':
    sys.exit(main())
