#!/bin/sh
# ./bt-device remove xx:xx:xx:xx:xx:xx
#

REMOVE="./bt-device remove"
LIST="./bt-device list"

devices=`eval $LIST | cut -d' ' -f1`
echo $devices

for dev in $devices; do 
	# echo "Remove $dev"
	eval $REMOVE $dev
done

