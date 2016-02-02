#
# Reflects the partial 3d grid for C2 c9h9+ as
# (x,y,z) -> (-x,-y,z)
# and prints GAUSSIAN cube data in x, y, z order
# (z changes fastest, followed by y and x)
#
import os
import sys
import csv

# nx = 70
# ny = 90
# nz = 70
# dalta = 0.05
# it = int
ix = []
iy = []
iz = []
br = 0.5291772083
nx = 70
ny = 90
nz = 70
delta = 0.05
def GridGen():
    nx = 70
    ny = 90
    nz = 70
    dalta = 0.05
    globals
    for x in range(-nx,nx+1,1):
        x = x * dalta
        for y in range(-ny,ny+1,1):
            y = y * dalta
            for z in range(-nz,nz+1,1):
                z = z * dalta
                ix.append("%.6f" % x)
                iy.append("%.6f" % y)
                iz.append("%.6f" % z)
    return ix, iy, iz

GridGen()
print(ix[1])
with open('cube_grid', 'w', newline='') as csvfile:
    cubewriter = csv.writer(csvfile, delimiter='\t',
                            quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    for i in range(len(ix)):
        cubewriter.writerow([ix[i], iy[i], iz[i]])
    pass

