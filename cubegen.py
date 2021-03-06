#
# Reflects the partial 3d grid for C2 c9h9+ as
# (x,y,z) -> (-x,-y,z)
# and prints GAUSSIAN cube data in x, y, z order
# (z changes fastest, followed by y and x)
#
import os
import sys
import csv


MAXCOLS = 9
cols = [[] for _ in range(MAXCOLS)]
with open('grid', 'r') as data:
    for row in csv.reader(data, delimiter='\t'):
        for i in range(MAXCOLS):
            cols[i].append(row[i] if i < len(row) else '')


# change cols[i] data type into float
data4 = list(map(float, cols[3]))

print(len(data4))

# set xyz lists and C2 opreating
siso = []
br = 0.5291772083
nx = 70
ny = 90
nz = 70
delta = 0.05

# change float digits into 6
for d in range(len(data4)):
    sisodata = "%.6f" % data4[d]
    siso.append(sisodata)

# write cube file
with open('cube.cube', 'w', newline='') as csvfile:
    cubewriter = csv.writer(csvfile, delimiter='\t',
                            quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    cubewriter.writerow(['C9H9+ HF/6-311++G(d,p) nmr partial 3d grid'])
    cubewriter.writerow(['OUTER LOOP: X, MIDDLE '
                         'LOOP: Y, INNER LOOP: Z'])
    # NAtoms, X-Origin, Y-Origin, Z-Origin NVal
    cubewriter.writerow([18, "%.6f" % (-nx * delta / br), "%.6f" % (-ny * delta / br),
                         "%.6f" % ((-nz + 10) * delta / br)])
    # N1, X1, Y1, Z1               # of increments in the slowest running direction
    # N2, X2, Y2, Z2
    # N3, X3, Y3, Z3               # of increments in the fastest running direction
    cubewriter.writerow([2 * nx + 1, "%.6f" % (delta / br), "%.6f" % 0.000000, "%.6f" % 0.000000])
    cubewriter.writerow([2 * ny + 1, "%.6f" % 0.0, "%.6f" % (delta / br), "%.6f" % 0.0])
    cubewriter.writerow([2 * nz + 1, "%.6f" % 0.000000, "%.6f" % 0.000000, "%.6f" % (delta / br)])
    # geo of c9h9+
    # IA1, Chg1, X1, Y1, Z1        Atomic number, charge, and coordinates of the first atom
    # …
    # IAn, Chgn, Xn, Yn, Zn        Atomic number, charge, and coordinates of the last atom
    cubewriter.writerow([6, "%.6f" % 6.0, "%.6f" % (0.0/br), "%.6f" % (0.0/br), "%.6f" % (1.645014194/br)])
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
    cubewriter2 = csv.writer(csvfile, delimiter=' ',
                        quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    for c in range(0, len(siso), 6):
        rest2 = len(siso) % 6
        if c + 6 + rest2 <= len(siso):
            cubewriter2.writerow([siso[c+p] for p in range(6)])
        else:
            cubewriter2.writerow([siso[c], siso[c + 1], siso[c + 2]])
    pass
csvfile.close()
print(len(siso))
