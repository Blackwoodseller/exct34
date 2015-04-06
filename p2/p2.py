#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Make a file result.txt contains a list of words’ lengths in the text
(sorted ascendingly) and number of its occurrence: “length ­ amount”

"""
import re
import os.path

delim = re.compile(r'[^a-zA-Z0-9\s]')

with open(name=os.path.join(os.path.dirname(__file__), 'something.txt'), mode='r') as f1:
    # in next line we will read whole file, replace ends of lines with space,
    # remove punctuations, split file content into a words' list
    # and map list items with words' lengths.
    a = map(lambda x: len(x), re.sub(delim, '', f1.read().replace('\n',' ')).lower().split(' '))

    # sorted dict of distinct words lengths
    b = dict(zip(a, a))

    with open(name=os.path.join(os.path.dirname(__file__),'result.txt'), mode='w') as f2:
        for i in b:
            f2.write('%d - %d\n' % (i, a.count(i)))
