#
# Reflects the partial 3d grid for C2 c9h9+ as
# (x,y,z) -> (-x,-y,z)
# and prints GAUSSIAN cube data in x, y, z order
# (z changes fastest, followed by y and x)
import csv
import operator

M = []
N = []

data = open('unformartcube2.cube', 'r')
csv1 = csv.reader(data, delimiter='\t')

for i in csv1:
    N = list(map(float, i))
    M.append(N)

sort0 = sorted(M, key=operator.itemgetter(0, 1, 2))

with open('grid', 'w', newline='') as csvfile:
    cubewriter = csv.writer(csvfile, delimiter='\t',
                            quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    for eachline in sort0:
        cubewriter.writerow(eachline)
    pass



