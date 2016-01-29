import os
import sys
import csv
import copy

skip = 0


def main():

    global idx
    f = open('c2','r')

    while f:
        line = f.readline()
        try:
            x, y, z, siso  = [100 * float(v) for v in line.split(",")]

            idx = int(idx)
            if (x * y * z != 0):


            points.append(v)
        except ValueError:
            break


class CubefileHeader:

    for i in range(skip):
            f.readline()

        index += 1

    f.close()

    return
