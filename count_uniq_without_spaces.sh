#!/bin/bash

source /opt/libs/source.bash
source /etc/profile.d/00-functions.sh

cat $1 | sort | uniq -c | awk '{print $1","$2}' | awk -F, '{print $2","$3","$4","$5","$1","$6}' > hello.data
cat header hello.data > $2