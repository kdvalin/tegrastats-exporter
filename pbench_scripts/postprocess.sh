#!/bin/bash

SCRIPT_DIR=$(dirname -- "$0")

out_dir=$1

$SCRIPT_DIR/../parser.py -i $out_dir/tegrastats.log -o $out_dir/tegrastats.csv
