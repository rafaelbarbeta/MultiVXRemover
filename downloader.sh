#!/bin/bash

mkdir VirusShareHashes
cd VirusShareHashes
url=https://virusshare.com/hashfiles/VirusShare_
for i in $(seq -w 0 99999) ; do
    nexturl=""
    nexturl+=$url
    nexturl+=$i
    nexturl+=".md5"
    wget $nexturl
    if [ $? -ne 0 ] ; then
        break
    fi
done