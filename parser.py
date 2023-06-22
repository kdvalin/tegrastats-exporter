#!/usr/bin/env python3
import sys
import stats

def parse_file(filename):
    cont = stats.StatContainer()
    with open(filename, 'r') as f:
        for line in f.readlines():
            args = line.strip().split(' ')

            timestamp = args[0:1]

            for i in range(len(args)):
                key = args[i]
                stat_cont = cont.find_stat(key)

                if stat_cont is not None:
                    print(f"{stat_cont.get_num_args()} | {len(args[i:i+stat_cont.get_num_args()])}")
                    print(stat_cont.parse(args[i:i+stat_cont.get_num_args()]))


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.stderr.write(f"Usage: {sys.argv[0]} <name of file to parse>\n")
        exit(1)
    parse_file(sys.argv[1])
