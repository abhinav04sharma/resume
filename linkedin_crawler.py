#!/usr/bin/python

import urllib2
import sys
from pyquery import PyQuery    

def download_page(url, data_dir):
    req = urllib2.Request(url, headers={ 'User-Agent': 'Mozilla/5.0' })
    page = urllib2.urlopen(req).read()
    fileHandle = open(data_dir + '/' + url.replace(':', '#').replace('/', '_'), 'w')
    print >> fileHandle, page
    fileHandle.close();


root_url = sys.argv[1]

if root_url == '--help':
    print 'Useage: python linkedin_crawler.py <root_profile> <depth> <data_dir>'
    exit(0)

count = int(sys.argv[2])
data_dir = sys.argv[3]

list = []
list.append(root_url)

while count > 0:
    url=list.pop(0)

    pq = PyQuery(url)
    for link in pq('li.with-photo strong a'):
        if link.attrib['href'] not in list:
            list.append(link.attrib['href'])
    count = count - 1

for url in list:
    download_page(url, data_dir)

print "\n".join(list)
