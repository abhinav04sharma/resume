#!/usr/bin/python

import os
import sys
from pyquery import PyQuery    
import pdb
import json

def extract_row(html, config_file):
    #pdb.set_trace()
    pq = PyQuery(html)
    #row = []
    row = {}
    configs = [line.strip() for line in open(config_file)]
    for config in configs:
        tags = pq(config)
        feature = []
        for tag in tags:
            feature.append(pq(tag).text())
        #row.append(feature)
        row[config] = feature
    return json.dumps(row, ensure_ascii=True)

config_file = sys.argv[1]
if config_file == '--help' or len(sys.argv) != 3:
    print 'Useage: python parse_html.py <config_file> <data_dir>'
    exit(0)

data_dir = sys.argv[2]

for data_file in os.listdir(data_dir):
    with open (data_dir + '/' + data_file, 'r') as myfile:
        html=myfile.read().replace('\n', '')
    print extract_row(html, config_file)
