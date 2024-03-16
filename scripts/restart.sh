#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 <var>"
    exit 1
fi

var=$1

docker restart "${var}-1"
