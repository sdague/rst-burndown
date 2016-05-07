#!/usr/bin/env python

import collections
import time
import glob

TOP = 'nova/api-ref/source'

counts = collections.OrderedDict()
counts['needs:method_verification'] = []
counts['needs:parameter_verification'] = []
counts['needs:example_verification'] = []
counts['needs:body_verification'] = []
# counts['done'] = []

for fname in glob.glob("%s/*.inc" % TOP):
# current_file = os.path.join(TOP, fname)
    with open(fname) as f:
        content = f.readlines()
        done = True
        for key in counts.keys():
            if ".. %s\n" % key in content:
                done = False
                counts[key].append(fname)
        if done:
            counts['done'].append(fname)

with open("data.csv", "a") as f:
    f.write("%d,%d,%d,%d,%d\n" % (
        int(time.time()),
        len(counts['needs:method_verification']),
        len(counts['needs:parameter_verification']),
        len(counts['needs:example_verification']),
        len(counts['needs:body_verification'])))


# print int(time.time())

# for k, v in counts.items():
#     print "%-30s %3s" % (k, len(v))
