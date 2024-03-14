#!/bin/bash

REGION=$1

region_list="data/lists/${REGION}.txt"

make list-region region=$REGION

cat $region_list | xargs -P 10 -t -I % make get-data region=${REGION} workunit=%