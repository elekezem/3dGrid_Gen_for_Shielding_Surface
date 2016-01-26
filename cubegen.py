import os
import csv
import numpy

MAXCOLS = 9
cols = [[] for _ in range(MAXCOLS)]
with open('c2', 'r') as input:
    for row in csv.reader(input, delimiter=' '):
        for i in range(MAXCOLS):
            cols[i].append(row[i] if i < len(row) else '')

# for i in range(MAXCOLS):
#     print('cols[{}]: {}'.format(i, cols[i]))
x = list(map(float, cols[1]))
y = list(map(float, cols[2]))
z = list(map(float, cols[3]))
siso = list(map(float, cols[4]))

nx = []
ny = []
nz = []
nsiso = []

br = 0.5291772083
delta = 0.05
for k in range(len(x)):
    nx.append(k)
    ny.append(k)
    nz.append(k)
    nsiso.append(k)
    nx[k] = x[k]*-1
    ny[k] = y[k]*-1
    nz[k] = z[k]*1
    nsiso[k] = siso[k]*1
with open('cube.cube', 'w', newline='') as csvfile:
    cubewriter = csv.writer(csvfile, delimiter=' ',
                            quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    cubewriter.writerow(['C9H9+ HF/6-311++G(d,p) nmr partial 3d grid'])
    cubewriter.writerow(['x,y,z: -3.5(0.05)3.5 A '
                         'exp. geom. (1.3964/1.0831)'])

    # for c in range(len(x)):
    for c in range(100):
        cubewriter.writerow([x[c], y[c], z[c], siso[c]])
    pass
    # for nc in range(len(nx)):
    for nc in range(100):
        cubewriter.writerow([nx[nc], ny[nc], nz[nc], nsiso[nc]])
    pass
csvfile.close()