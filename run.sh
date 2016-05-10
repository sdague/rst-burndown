#!/bin/bash

set -e

cd $(dirname $0)
pushd nova
git pull > /dev/null
popd
./api-ref-burndown.py
git ci -m "Updated csv" > /dev/null
