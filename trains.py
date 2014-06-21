#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'billyevans'

import sys

from core.digraphio import parse_edgelist
import request


# main application
# accept 3 args
# 1st - graph file
# 2nd - requests
# 3rd - requests out

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: " + sys.argv[0] + " <graph> <requests> <result>")
        sys.exit(1)
    with open(sys.argv[1]) as gfile:
        G = parse_edgelist(gfile.readlines())

    with open(sys.argv[3], "w") as ofile:
        # process requests from file
        with open(sys.argv[2]) as rfile:
            for line in rfile:
                res = request.process(G, line)
                ofile.write(str(res) + '\n')
