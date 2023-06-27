#!/bin/bash

out_dir=$1
interval=$2

if  ! command -v tegrastats > /dev/null; then
    echo "Missing tegrastats"
    exit 1
fi

tegrastats --start --logfile $out_dir/tegrastats.log --interval $((interval*1000))

