#!/usr/bin/env python3
import sys
import stats
import csv

def parse_file(filename):
    cont = stats.StatContainer()
    with open(filename, 'r') as f:
        lines = f.readlines()

    first_line = True
    keys = ["Time"]
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
        with open("out.csv", "w" if first_line else "a+", newline="") as out:
            csvwriter = csv.writer(out)
            if first_line:
                csvwriter.writerow(keys)
                first_line = False
            csvwriter.writerow(row)
            



if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.stderr.write(f"Usage: {sys.argv[0]} <name of file to parse>\n")
        exit(1)
    parse_file(sys.argv[1])
