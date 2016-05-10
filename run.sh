#!/bin/bash

set -e

cd $(dirname $0)
pushd nova > /dev/null
git pull > /dev/null
popd > /dev/null
./api-ref-burndown.py
git ci -m "Updated csv" > /dev/null
