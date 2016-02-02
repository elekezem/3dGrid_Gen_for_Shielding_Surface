#
# Reflects the partial 3d grid for C2 c9h9+ as
# (x,y,z) -> (-x,-y,z)
# and prints GAUSSIAN cube data in x, y, z order
# (z changes fastest, followed by y and x)
import csv
import operator

data = open('c2f', 'r')
csv1 = csv.reader(data, delimiter=' ')

sort0 = sorted(csv1, key=operator.itemgetter(1))
print(sort0)
with open('grid', 'w', newline='') as csvfile:
    cubewriter = csv.writer(csvfile, delimiter='\t',
                            quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    for eachline in sort0:
        cubewriter.writerow(eachline)
    pass



