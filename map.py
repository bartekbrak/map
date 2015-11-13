#!/usr/bin/env python3
import sys
import time
from ast import literal_eval


def main():
    if len(sys.argv) != 2:
        sys.stderr.write('Provide a map file.\n')
        sys.exit(1)
    map_file = open(sys.argv[1]).read()
    map_ = literal_eval(map_file)

    for line in sys.stdin:
        if line.rstrip() in map_:
            line = map_[line.rstrip()] + '\n'
            sys.stdout.write(line)
            sys.stdout.flush()
        else:
            sys.stdout.write(line)
            sys.stdout.flush()

if __name__ == '__main__':
    main()
