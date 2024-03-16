#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 <var>"
    exit 1
fi

var=$1

git -C /root/code/"$var"_code pull

docker container rm -f "${var}-1" >/dev/null 2>&1 || true

docker build -t "$var" "/root/code/${var}_code"
docker run -d --name "${var}-1" "$var"
