#!/bin/bash

source /opt/libs/source.bash
source /etc/profile.d/00-functions.sh

# That's code execute before, don't uncommitted it
#cat $1 | sort | uniq -c | awk '{print $1","$2" "$3" "$4}' > hello.data

cat hello.data | awk -F, '{print $2","$3","$4","$5","$1","$6}' > kek.data
cat header kek.data > $2