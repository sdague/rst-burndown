#!/usr/bin/env python

import collections
import time
import glob
import os

TOP = 'nova/api-ref/source'

PHASES = ['needs:method_verification', 'needs:parameter_verification',
          'needs:example_verification', 'needs:body_verification']

counts = collections.OrderedDict()
for phase in PHASES:
    counts[phase] = []
counts['done'] = []

files = []

for fname in sorted(glob.glob("%s/*.inc" % TOP)):
    with open(fname) as f:
        fdata = {'filename': os.path.basename(fname)}
        content = f.readlines()
        done = True
        for key in PHASES:
            if ".. %s\n" % key in content:
                fdata[key] = "TODO"
                done = False
                counts[key].append(fname)
            else:
                fdata[key] = u"\u2713"
        if done:
            counts['done'].append(fname)
        files.append(fdata)

with open("data.csv", "a") as f:
    f.write("%d,%d,%d,%d,%d\n" % (
        int(time.time()),
        len(counts['needs:method_verification']),
        len(counts['needs:parameter_verification']),
        len(counts['needs:example_verification']),
        len(counts['needs:body_verification'])))


with open("data.txt", "w") as f:
    FORMAT = "%-40s %10s %10s %10s %10s\n"
    f.write(FORMAT % ("File Name", "Method", "Param", "Example", "Body"))
    for fdata in files:
        f.write((FORMAT % (fdata['filename'],
                           fdata['needs:method_verification'],
                           fdata['needs:parameter_verification'],
                           fdata['needs:example_verification'],
                           fdata['needs:body_verification'])).encode('utf8'))
