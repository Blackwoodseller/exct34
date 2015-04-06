#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Store information about RAM, CPUs, HDD usage in XML file.

    python sysinfo2xml xml_file_name | --help
"""
import sys
import getopt
import psutil
from lxml import etree


class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg


def bytes2human(n):
    # http://code.activestate.com/recipes/578019
    # >>> bytes2human(10000)
    # '9.8K'
    # >>> bytes2human(100001221)
    # '95.4M'
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' % (value, s)
    return "%sB" % n


def getsysreport():
    # returns dict with information about RAM, CPUs, HDD usage
    vm = psutil.virtual_memory()
    hdd = psutil.disk_usage('/')

    sys_report = {'RAM': {'Free': bytes2human(vm.free),
                          'Used': bytes2human(vm.used),
                          'Total': bytes2human(vm.total)}}
    sys_report['CPU'] = {}
    for i, percent in enumerate(psutil.cpu_percent(interval=1, percpu=True)):
        sys_report['CPU']['cpu' + str(i+1)] = str(percent) + '%'
    hdd = psutil.disk_usage('/')

    sys_report['HDD'] = {'Free': bytes2human(hdd.free),
                         'Used': bytes2human(hdd.used),
                         'Total': bytes2human(hdd.total)}
    return sys_report


def writereport(sys_report, filename):
    # Store information about RAM, CPUs, HDD usage in XML filename

    page = etree.Element('results')

    # Make a new document tree
    doc = etree.ElementTree(page)

    # Add the subelements
    for key in sys_report:
        etree.SubElement(page, key, sys_report[key])

    try:
        doc.write(filename, xml_declaration=True, encoding='utf-8', pretty_print=True)
    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)


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

    if len(args) != 1:
        print __doc__
        sys.exit(0)

    xml_file_name = args[0]

    try:
        with open(name=xml_file_name, mode='w') as f:
            pass
    except:
        print xml_file_name + " is not valid path."
        sys.exit(2)

    writereport(getsysreport(), xml_file_name)


if __name__ == '__main__':
    sys.exit(main())
