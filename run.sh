#!/bin/bash

set -e

cd $(dirname $0)
cd nova
git pull
cd ..
./api-ref-burndown.py
git ci -m "Updated csv"
