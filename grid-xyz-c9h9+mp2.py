#
# Reflects the partial 3d grid for C2 c9h9+ as
# (x,y,z) -> (-x,-y,z)
# and prints GAUSSIAN cube data in x, y, z order
# (z changes fastest, followed by y and x)
import csv
import operator


ix = []
iy = []
iz = []
siso = []
br = 0.5291772083
nx = 70
ny = 90
nz = 70
delta = 0.05


MAXCOLS = 9
cols = [[] for _ in range(MAXCOLS)]
with open('c2', 'r') as input:
    for row in csv.reader(input, delimiter=' '):
        for i in range(MAXCOLS):
            cols[i].append(row[i] if i < len(row) else '')

data1 = list(map(float, cols[1]))
data2 = list(map(float, cols[2]))
data3 = list(map(float, cols[3]))
data4 = list(map(float, cols[4]))
print(cols[1][1])
print(cols[2][1])
print(cols[3][1])
print(cols[4][1])



def grid_gen():
    for x in range(-nx, nx + 1, 1):
        x = x * delta
        for y in range(-ny, ny + 1, 1):
            y = y * delta
            for z in range(-nz + 10, nz + 11, 1):
                z = z * delta
                ix.append(round(x, 6))
                iy.append(round(y, 6))
                iz.append(round(z, 6))
    return ix, iy, iz


# def data_out():
#     for k in range(5000):
#         for j in range(5000):
#             if ix[k] == data1[j]:
#                 siso.append(data4[j])
#     return siso


########################################################################################
grid_gen()
# data_out()
print(len(ix))
print(len(data1))
print(len(siso))
with open('cube_grid', 'w', newline='') as csvfile:
    cubewriter = csv.writer(csvfile, delimiter='\t',
                            quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    for i in range(100):
        cubewriter.writerow([siso[i]])
    pass

