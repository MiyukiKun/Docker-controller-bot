#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 <var>"
    exit 1
fi

var=$1

docker container rm -f "${var}-1"

docker image rm "${var}"
