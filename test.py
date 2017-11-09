#! /usr/bin/env python3

import os
import pyvql
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: {} <vql_query>'.format(sys.argv[0].rsplit(os.sep, 1)[-1]), file=sys.stderr)
        sys.exit(1)

    print(pyvql.parse(sys.argv[1]))
