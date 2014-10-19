#!/usr/bin/python

import json
import sys

json_file = sys.argv[1]

with open(json_file) as f:
    lines = f.readlines()
    for line in lines:
        row = []
        obj = json.loads(line)
        row.append(','.join(obj['span.given-name']))
        row.append(','.join(obj['span.family-name']))
        row.append(','.join(obj['span.locality']))
        row.append(','.join(obj['dd.industry']))
        row.append(','.join(obj['h3.summary.fn.org'][0:1]))
        count = len(obj['div.postitle span.org.summary']) - 1
        while count >= 0:
            if obj['div.postitle span.org.summary'][count] != obj['div.postitle span.org.summary'][count - 1]:
                print '\t'.join(row) + '\t' + obj['div.postitle span.org.summary'][count] + '\t' + obj['div.postitle span.org.summary'][count- 1]
            count = count - 1
