#
# Reflects the partial 3d grid for D2d C3H4 as
# (x,y,z) -> (-x,-y,z)
# and prints GAUSSIAN cube data in x, y, z order
# (z changes fastest, followed by y and x)
#
import os
import sys
import csv


MAXCOLS = 9
cols = [[] for _ in range(MAXCOLS)]
with open('fullgrid', 'r') as data:
    for row in csv.reader(data, delimiter=','):
        for i in range(MAXCOLS):
            cols[i].append(row[i] if i < len(row) else '')

# change cols[i] data type into float
data4 = list(map(float, cols[3]))

print(len(data4))

# set xyz lists and D2d opreating
siso = []
br = 0.5291772083
nx = 59
ny = 59
nz = 59
delta = 0.05

# change float digits into 6
for d in range(len(data4)):
    sisodata = "%.6f" % data4[d]
    siso.append(sisodata)

# write cube file
with open('cube.cube', 'w', newline='') as csvfile:
    cubewriter = csv.writer(csvfile, delimiter='\t',
                            quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    cubewriter.writerow(['C3H4 MP2/6-311++G(d,p) nmr partial 3d grid'])
    cubewriter.writerow(['OUTER LOOP: X, MIDDLE '
                         'LOOP: Y, INNER LOOP: Z'])
    # NAtoms, X-Origin, Y-Origin, Z-Origin NVal
    cubewriter.writerow([7, "%.6f" % (-nx * delta / br), "%.6f" % (-ny * delta / br),
                         "%.6f" % (-nz * delta / br)])
    # N1, X1, Y1, Z1               # of increments in the slowest running direction
    # N2, X2, Y2, Z2
    # N3, X3, Y3, Z3               # of increments in the fastest running direction
    cubewriter.writerow([2*nx + 1, "%.6f" % (delta / br), "%.6f" % 0.000000, "%.6f" % 0.000000])
    cubewriter.writerow([2*ny + 1, "%.6f" % 0.000000, "%.6f" % (delta / br), "%.6f" % 0.000000])
    cubewriter.writerow([2*nz + 1, "%.6f" % 0.000000, "%.6f" % 0.000000, "%.6f" % (delta / br)])

    # geo of c3h4
    # IA1, Chg1, X1, Y1, Z1        Atomic number, charge, and coordinates of the first atom
    # …
    # IAn, Chgn, Xn, Yn, Zn        Atomic number, charge, and coordinates of the last atom

    cubewriter.writerow([6,"%.6f" % 6.0,"%.6f" % (0.0000000/br),"%.6f" % (1.30910000/br),"%.6f" % (0.00000000/br)])
    cubewriter.writerow([6,"%.6f" % 6.0,"%.6f" % (0.0000000/br),"%.6f" % (0.00000000/br),"%.6f" % (0.00000000/br)])
    cubewriter.writerow([6,"%.6f" % 6.0,"%.6f" % (0.0000000/br),"%.6f" % (-1.30910000/br),"%.6f" % (0.00000000/br)])
    cubewriter.writerow([1,"%.6f" % 1.0,"%.6f" % (0.0000000/br),"%.6f" % (1.86625769/br),"%.6f" % (0.93241930/br)])
    cubewriter.writerow([1,"%.6f" % 1.0,"%.6f" % (0.0000000/br),"%.6f" % (1.86625769/br),"%.6f" % (-0.93241930/br)])
    cubewriter.writerow([1,"%.6f" % 1.0,"%.6f" % (-0.9324193/br),"%.6f" % (-1.86625769/br),"%.6f" % (0.00000000/br)])
    cubewriter.writerow([1,"%.6f" % 1.0,"%.6f" % (0.9324193/br),"%.6f" % (-1.86625769/br),"%.6f" % (0.00000000/br)])

    # (N1*N2) records, each of length N3     Values of the density at each point in the grid
    cubewriter2 = csv.writer(csvfile, delimiter=' ',
                        quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    for c in range(0, len(siso), 6):
        rest2 = len(siso) % 6
        if c + 6 + rest2 <= len(siso):
            cubewriter2.writerow([siso[c+p] for p in range(6)])
        else:
            cubewriter2.writerow([siso[c], siso[c + 1], siso[c + 2],siso[c + 3],siso[c + 4]])
    pass
csvfile.close()
