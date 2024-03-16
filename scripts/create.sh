#!/bin/bash

if [ $# -ne 3 ]; then
    echo "Usage: $0 <git_link> <var> <env>"
    exit 1
fi

git_link=$1
var=$2
env=$3

git clone "$git_link" "/root/code/${var}_code"

echo -e "$env" > "/root/code/${var}_code/.env"

docker build -t "$var" "/root/code/${var}_code"
docker run -d --name "${var}-1" "$var"
