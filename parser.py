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

def build_args(args: List[str], stat: stats.NvidiaStat, current: int):
    stat_args = stat.get_num_args()

    if stat_args < 0:
        start = current + stat_args + 1
        end = current + 1
    else:
        start = current
        end = current + stat_args

    return args[start:end]

def get_keys(file: str, stats_container: stats.StatContainer) -> List[str]:
    keys = ["Time"]
    with open(file, 'r') as file:
        for line in file:
            args = line.strip().split(' ')

            for i in range(len(args)):
                final_stat = None
                stat_args = []
                for stat_cont in stats_container.find_stat(args[i]):         
                    #Done to support backwards matching (IE easier to match against the 2nd+ arg instead of the first)
                    stat_args = build_args(args, stat_cont, i)
                    if stat_cont.args_match(stat_args):
                        final_stat = stat_cont

                if final_stat is not None:
                    data = final_stat.parse(build_args(args, final_stat, i))
                    for key in data:
                        keyname = key[0]

                        if keyname in keys:
                            continue

                        keys.extend([keyname])
    return keys


def parse_file(input_file: str):
    logger = logging.getLogger(__package__)
    cont = stats.StatContainer()
    with open(input_file, 'r') as f:
        lines = f.readlines()

    keys = get_keys(input_file, cont)
    
    rows = []

    for line in lines:
        args = line.strip().split(' ')
        timestamp = args[0:2]
        row = [-1 for _ in keys]
        row[0] = ' '.join(timestamp)
        
        for i in range(len(args)):
            key = args[i]
            final_stat = None
            stat_args = []
            for stat_cont in cont.find_stat(key):         
                #Done to support backwards matching (IE easier to match against the 2nd+ arg instead of the first)
                stat_args = build_args(args, stat_cont, i)
                if stat_cont.args_match(stat_args):
                    final_stat = stat_cont

            if final_stat is None:
                logger.debug(f"Could not find match for {key}")
                continue
            data = final_stat.parse(stat_args)

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
    logging.basicConfig(level=os.environ.get("LOGLEVEL", "WARNING").upper())
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
