#!/usr/bin/env python3
from typing import List
import sys
import stats
import csv

def write_file(header: List[str], rows: List[list], output_file: str):
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)


def parse_file(input_file: str):
    cont = stats.StatContainer()
    with open(input_file, 'r') as f:
        lines = f.readlines()

    first_line = True
    keys = ["Time"]
    rows = []
    for line in lines:
        args = line.strip().split(' ')
        timestamp = args[0:2]
        row = [' '.join(timestamp)]
        
        for i in range(len(args)):
            key = args[i]
            stat_cont = cont.find_stat(key)

            if stat_cont is not None:
                data = stat_cont.parse(args[i:i+stat_cont.get_num_args()])
                if first_line:
                    keys.extend([i[0] for i in data])
                row.extend([i[1] for i in data])
        rows.append(row)
        first_line = False

    return keys, rows
            



if __name__ == "__main__":
    if len(sys.argv) <= 2:
        sys.stderr.write(f"Usage: {sys.argv[0]} <name of file to parse> <output file name>\n")
        exit(1)
    header, rows = parse_file(sys.argv[1])
    write_file(header, rows, sys.argv[2])
