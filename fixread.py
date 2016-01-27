import os
import sys
import csv
import copy

skip = 0

class cubefile_header:


def main():

    f = open('c2','r')

    while f:
        line = f.readline()
        try:
            x, y, z, siso  = [100 * float(v) for v in line.split(",")]

            idx = int(idx)
            if (x * y * z != 0):
                bs.Select(index)

            points.append(v)
        except ValueError:
            break

        for i in range(skip):
            f.readline()

        index += 1

    f.close()

    return
