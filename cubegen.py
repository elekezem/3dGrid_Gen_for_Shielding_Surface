#
# Reflects the partial 3d grid for D6h benzene as
# (x,y,z) -> (-x,-y,z)
# and prints GAUSSIAN cube data in x, y, z order
# (z changes fastest, followed by y and x)
#
import os
import csv
import numpy
import math
import decimal
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
x = []
y = []
z = []
siso = []
mx = []
my = []
mz = []
msiso = []
br = 0.5291772083
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
    x.append(xdata)
    y.append(ydata)
    z.append(zdata)
    siso.append(sisodata)
    mx.append(mxdata)
    my.append(mydata)
    mz.append(mzdata)
    msiso.append(msisodata)

# write cube file
with open('cube.cube', 'w', newline='') as csvfile:
    cubewriter = csv.writer(csvfile, delimiter=' ',
                            quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    cubewriter.writerow(['C9H9+ HF/6-311++G(d,p) nmr partial 3d grid'])
    cubewriter.writerow(['x,y,z: -3.5(0.05)3.5 A '
                         'exp. geom. (1.3964/1.0831)'])
    cubewriter.writerow([18])
    # for c in range(len(x)):
    for c in range(100):
        cubewriter.writerow([x[c], y[c], z[c], siso[c]])
    pass
    # for nc in range(len(nx)):
    for nc in range(100):
        cubewriter.writerow([mx[nc], my[nc], mz[nc], msiso[nc]])
    pass
csvfile.close()
