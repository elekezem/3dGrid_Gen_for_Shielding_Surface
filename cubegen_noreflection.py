#
# Reflects the partial 3d grid for C2 c9h9+ as
# (x,y,z) -> (-x,-y,z)
# and prints GAUSSIAN cube data in x, y, z order
# (z changes fastest, followed by y and x)
#
import os
import sys
import csv
import copy
import math
import decimal
import numpy
from _decimal import *

MAXCOLS = 9
cols = [[] for _ in range(MAXCOLS)]
with open('c2', 'r') as input:
    for row in csv.reader(input, delimiter=' '):
        for i in range(MAXCOLS):
            cols[i].append(row[i] if i < len(row) else '')
# for i in range(MAXCOLS):
#     print('cols[{}]: {}'.format(i, cols[i]))

# change cols[i] data type into float
data1 = list(map(float, cols[1]))
data2 = list(map(float, cols[2]))
data3 = list(map(float, cols[3]))
data4 = list(map(float, cols[4]))
data5 = []
data6 = []
data7 = []
data8 = []

# set xyz lists and C2 opreating
x_loop = []
y_loop = []
z_loop = []
siso = []
mx = []
my = []
mz = []
msiso = []
br = 0.5291772083
nx = 70
ny = 90
nz = 70
delta = 0.05


# reflect (x,y,z) to (-x,-y,z), a C2 operating
for k in range(len(data1)):
    data5.append(k)
    data6.append(k)
    data7.append(k)
    data8.append(k)
    data5[k] = data1[k] * -1
    data6[k] = data2[k] * -1
    data7[k] = data3[k] * 1
    data8[k] = data4[k] * 1

# change float digits into 6
for d in range(len(data1)):
    xdata = "%.6f" % data1[d]
    ydata = "%.6f" % data2[d]
    zdata = "%.6f" % data3[d]
    sisodata = "%.6f" % data4[d]
    mxdata = "%.6f" % data5[d]
    mydata = "%.6f" % data6[d]
    mzdata = "%.6f" % data7[d]
    msisodata = "%.6f" % data8[d]
    x_loop.append(xdata)
    y_loop.append(ydata)
    z_loop.append(zdata)
    siso.append(sisodata)
    mx.append(mxdata)
    my.append(mydata)
    mz.append(mzdata)
    msiso.append(msisodata)

# write cube file
with open('cube_noreflaction.cube', 'w', newline='') as csvfile:
    cubewriter = csv.writer(csvfile, delimiter='\t',
                            quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    cubewriter.writerow(['C9H9+ HF/6-311++G(d,p) nmr partial 3d grid'])
    cubewriter.writerow(['OUTER LOOP: X, MIDDLE '
                         'LOOP: Y, INNER LOOP: Z'])
    # NAtoms, X-Origin, Y-Origin, Z-Origin NVal
    cubewriter.writerow([18, "%.6f" % (-nx * delta / br), "%.6f" % 0.0,
                         "%.6f" % ((-nz + 10) * delta / br)])
    # N1, X1, Y1, Z1               # of increments in the slowest running direction
    # N2, X2, Y2, Z2
    # N3, X3, Y3, Z3               # of increments in the fastest running direction
    cubewriter.writerow([2 * nx + 1, "%.6f" % (delta / br), "%.6f" % 0.000000, "%.6f" % 0.000000])
    cubewriter.writerow([1 * ny + 1, "%.6f" % 0.0, "%.6f" % (delta / br), "%.6f" % 0.0])
    cubewriter.writerow([2 * nz + 1, "%.6f" % 0.000000, "%.6f" % 0.000000, "%.6f" % (delta / br)])
    # geo of c9h9+
    # IA1, Chg1, X1, Y1, Z1        Atomic number, charge, and coordinates of the first atom
    # …
    # IAn, Chgn, Xn, Yn, Zn        Atomic number, charge, and coordinates of the last atom
    cubewriter.writerow([6,"%.6f" % 6.0,"%.6f" % (0.0/br),"%.6f" % (0.0/br),"%.6f" % (1.645014194/br)])
    cubewriter.writerow(
            [6, "%.6f" % 6.0, "%.6f" % (0.4905022324 / br), "%.6f" % (1.2427684773 / br), "%.6f" % (1.1554414148/br)])
    cubewriter.writerow(
            [6, "%.6f" % 6.0, "%.6f" % (-0.4905022324 / br), "%.6f" % (-1.2427684773 / br), "%.6f" % (1.1554414148/br)])
    cubewriter.writerow(
            [6, "%.6f" % 6.0, "%.6f" % (0.0100585215 / br), "%.6f" % (2.0928052569 / br), "%.6f" % (0.1040785875/br)])
    cubewriter.writerow(
            [6, "%.6f" % 6.0, "%.6f" % (-0.0100585215 / br), "%.6f" % (-2.0928052569 / br), "%.6f" % (0.1040785875/br)])
    cubewriter.writerow(
            [6, "%.6f" % 6.0, "%.6f" % (-0.8152087457 / br), "%.6f" % (1.6410894083 / br), "%.6f" % (-0.9354914584/br)])
    cubewriter.writerow(
            [6, "%.6f" % 6.0, "%.6f" % (0.8152087457 / br), "%.6f" % (-1.6410894083 / br), "%.6f" % (-0.9354914584/br)])
    cubewriter.writerow(
            [6, "%.6f" % 6.0, "%.6f" % (-0.6569284614 / br), "%.6f" % (0.2832859329 / br), "%.6f" % (-1.251946014/br)])
    cubewriter.writerow(
            [6, "%.6f" % 6.0, "%.6f" % (0.6569284614 / br), "%.6f" % (-0.2832859329 / br), "%.6f" % (-1.251946014/br)])
    cubewriter.writerow([1, "%.6f" % 1.0, "%.6f" % (0. / br), "%.6f" % (0. / br), "%.6f" % (2.7459418542/br)])
    cubewriter.writerow(
            [1, "%.6f" % 1.0, "%.6f" % (1.0699783805 / br), "%.6f" % (1.7858874614 / br), "%.6f" % (1.9137457041/br)])
    cubewriter.writerow(
            [1, "%.6f" % 1.0, "%.6f" % (-1.0699783805 / br), "%.6f" % (-1.7858874614 / br), "%.6f" % (1.9137457041/br)])
    cubewriter.writerow(
            [1, "%.6f" % 1.0, "%.6f" % (0.12964425 / br), "%.6f" % (3.1677255378 / br), "%.6f" % (0.2859658405/br)])
    cubewriter.writerow(
            [1, "%.6f" % 1.0, "%.6f" % (-0.12964425 / br), "%.6f" % (-3.1677255378 / br), "%.6f" % (0.2859658405/br)])
    cubewriter.writerow(
            [1, "%.6f" % 1.0, "%.6f" % (-1.5936377795 / br), "%.6f" % (2.2790433661 / br), "%.6f" % (-1.3665504299/br)])
    cubewriter.writerow(
            [1, "%.6f" % 1.0, "%.6f" % (1.5936377795 / br), "%.6f" % (-2.2790433661 / br), "%.6f" % (-1.3665504299/br)])
    cubewriter.writerow(
            [1, "%.6f" % 1.0, "%.6f" % (-1.490812806 / br), "%.6f" % (-0.3325910524 / br), "%.6f" % (-1.6109751404/br)])
    cubewriter.writerow(
            [1, "%.6f" % 1.0, "%.6f" % (1.490812806 / br), "%.6f" % (0.3325910524 / br), "%.6f" % (-1.6109751404/br)])
    # (N1*N2) records, each of length N3     Values of the density at each point in the grid
    # for nc in range(0,len(msiso),6):
    #     rest = len(msiso) % 6
    #     if nc + 6 + rest <= len(msiso):
    #         cubewriter.writerow([msiso[nc+p] for p in range(6)])
    #     else:
    #         cubewriter.writerow([msiso[nc],msiso[nc + 1],msiso[nc + 2]])
    # pass
    for c in range(0,len(siso),6):
        rest2 = len(siso) % 6
        if c + 6 + rest2 <= len(siso):
            cubewriter.writerow([siso[c+p] for p in range(6)])
        else:
            cubewriter.writerow([siso[c],siso[c + 1],siso[c + 2]])
    pass
csvfile.close()

print(len(msiso))
