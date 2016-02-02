#
# Reflects the partial 3d grid for C2 c9h9+ as
# (x,y,z) -> (-x,-y,z)
# and prints GAUSSIAN cube data in x, y, z order
# (z changes fastest, followed by y and x)
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
MAXCOLS = 9
cols = [[] for _ in range(MAXCOLS)]


def read_out():
    with open('c2', 'r') as input:
        for row in csv.reader(input, delimiter=' '):
            for i in range(MAXCOLS):
                cols[i].append(row[i] if i < len(row) else '')
    return cols[4]


def grid_gen():
    nx = 70
    ny = 90
    nz = 70
    dalta = 0.05
    for x in range(-nx, nx + 1, 1):
        x = x * dalta
        for y in range(-ny, ny + 1, 1):
            y = y * dalta
            for z in range(-nz + 10, nz + 11, 1):
                z = z * dalta
                ix.append("%.6f" % x)
                iy.append("%.6f" % y)
                iz.append("%.6f" % z)
    return ix, iy, iz


########################################################################################
read_out()
grid_gen()
print(len(ix))
print(len(cols[4])*2)
with open('cube_grid', 'w', newline='') as csvfile:
    cubewriter = csv.writer(csvfile, delimiter='\t',
                            quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    for i in range(len(ix)):
        cubewriter.writerow([ix[i], iy[i], iz[i]])
    pass

