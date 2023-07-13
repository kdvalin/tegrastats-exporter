#!/usr/bin/env python3
import stats

from typing import List
import sys
import csv
import argparse
import logging
import os

def write_file(header: List[str], rows: List[list], output_file: str):
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)


def get_keys(line: str, stats_container: stats.StatContainer) -> List[str]:
    args = line.strip().split(' ')
    keys = ["Time"]

    for i in range(len(args)):
        stat = stats_container.find_stat(args[i])

        if stat is not None:
            stat_arg_end = i + stat.get_num_args()
            data = stat.parse(args[i:stat_arg_end])

            keys.extend([j[0] for j in data])
    return keys


def parse_file(input_file: str):
    cont = stats.StatContainer()
    with open(input_file, 'r') as f:
        lines = f.readlines()

    keys = get_keys(lines[0], cont)
    
    rows = []

    for line in lines:
        args = line.strip().split(' ')
        timestamp = args[0:2]
        row = [-1 for _ in keys]
        row[0] = ' '.join(timestamp)
        
        for i in range(len(args)):
            key = args[i]
            stat_cont = cont.find_stat(key)

            if stat_cont is None:
                continue
            data = stat_cont.parse(args[i:i+stat_cont.get_num_args()])

            for entry in data:
                header = entry[0]
                val = entry[1]

                val_idx = keys.index(header)

                if val_idx < 0:
                    keys.append(header)
                    val_idx = keys.index(header)
                row[val_idx] = val

        rows.append(row)
        first_line = False

    return keys, rows


if __name__ == "__main__":
    logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO").upper())
    logging.getLogger(__package__)
    
    parser = argparse.ArgumentParser(
        prog="tegrastats-exporter",
        description="A tool to transform tegrastats output to a csv"
    )
    parser.add_argument("-i", "--input", required=True, help="An input file generated by tegrastats")
    parser.add_argument("-o", "--output", required=True, help="The name of the CSV to be generated")
    args = parser.parse_args()

    header, rows = parse_file(args.input)
    write_file(header, rows, args.output)
