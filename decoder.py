#!/bin/python

import sys
import csv
import base64

f = open('dec', 'r')
reader = csv.reader(f)
d = open('impre.csv', 'w')
writer = csv.writer(d)

for row in reader:
    writer.writerow([base64.b64encode(row[0]), row[1], row[2], row[3], row[4]])