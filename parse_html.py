#!/usr/bin/python

import os
import sys
from pyquery import PyQuery    

data_dir = sys.argv[1]
if data_dir == '--help':
    print 'Useage: python parse_html.py <data_dir>'
    exit(0)

for data_file in os.listdir(data_dir):

    with open (data_dir + '/' + data_file, 'r') as myfile:
        html=myfile.read().replace('\n', '')

    pq = PyQuery(html)

    row = []

    row.append(pq('ul.current a span.org.summary').text())
    row.append(pq('span.locality').text())
    row.append(pq('dd.industry').text())
    print row
