#
# Reflects the partial 3d grid for C2 c9h9+ as
# (x,y,z) -> (-x,-y,z)
# and prints GAUSSIAN cube data in x, y, z order
# (z changes fastest, followed by y and x)
#
# TODO(sean): Use a "*" here for string repetition.
# TODO(abel) Change this to use relations.


import csv

# set xyz lists and C2 opreating
x_loop = []
y_loop = []
z_loop = []
siso = []
x_zero = []
y_zero = []
z_zero = []
siso_zero = []
neg_x_loop = []
neg_y_loop = []
neg_z_loop = []
neg_siso_loop = []
list_y_zero = []
items_in_list = 0

MAXCOLS = 9
cols = [[] for _ in range(MAXCOLS)]
with open('reflection-mp2.csv', 'r') as input:
    for row in csv.reader(input, delimiter=','):
        for i in range(MAXCOLS):
            cols[i].append(row[i] if i < len(row) else '')

# change cols[i] data type into float
ori_data_x = list(map(float, cols[0]))
ori_data_y = list(map(float, cols[1]))
ori_data_z = list(map(float, cols[2]))
ori_data_siso = list(map(float, cols[3]))
tmp_x = list(map(float, cols[0]))
tmp_y = list(map(float, cols[1]))
tmp_z = list(map(float, cols[2]))
tmp_siso = list(map(float, cols[3]))
neg_x = []
neg_y = []
neg_z = []
neg_siso = []
zero_x = []
zero_y = []
zero_z = []
zero_siso = []


for d in range(len(ori_data_x)):
    if ori_data_y[d] == 0.0:
        list_y_zero.append(d)
print('length of list_y_zero:', len(list_y_zero))

while items_in_list < len(tmp_y):
    if tmp_y[items_in_list] == 0.0:
        del tmp_y[items_in_list]
        del tmp_x[items_in_list]
        del tmp_z[items_in_list]
        del tmp_siso[items_in_list]
    else:
        items_in_list += 1
print('length of tmp_x:', len(tmp_x))
print(tmp_y[0])

# reflect (x,y,z) to (-x,-y,z), a C2 operating
for k in range(len(tmp_x)):
    neg_x.append(tmp_x[k] * -1)
    neg_y.append(tmp_y[k] * -1)
    neg_z.append(tmp_z[k] * 1)
    neg_siso.append(tmp_siso[k] * 1)
print('length of neg_x:', len(neg_x))
print(neg_y[0])

# while items_in_list < 1789288:
#     if tmp_y[items_in_list] > 0:
#         tmp_x.append(tmp_x[items_in_list] * -1)
#     # tmp_y.append(tmp_y[items_in_list] * -1)
#     # tmp_z.append(tmp_z[items_in_list] * 1)
#     # tmp_siso.append(tmp_siso[items_in_list] * 1)
#     else:
#         items_in_list += 1
# print(tmp_x[1789291])
# print('length of tmp_x:', len(tmp_x))

for z in list_y_zero:
    zero_x.append(ori_data_x[z])
    zero_y.append(ori_data_y[z])
    zero_z.append(ori_data_z[z])
    zero_siso.append((ori_data_siso[z]))

# def formart_digits(t, loop_t=None):
#     for d in range(len(t)):
#         data_t = "%.6f" % t[d]
#         loop_t.appnd(data_t)
#     return loop_t

# change float digits into 6
for d in range(len(tmp_x)):
    xdata = "%.6f" % tmp_x[d]
    ydata = "%.6f" % tmp_y[d]
    zdata = "%.6f" % tmp_z[d]
    sisodata = "%.6f" % tmp_siso[d]
    x_loop.append(xdata)
    y_loop.append(ydata)
    z_loop.append(zdata)
    siso.append(sisodata)

for d in range(len(zero_x)):
    mxdata = "%.6f" % zero_x[d]
    mydata = "%.6f" % zero_y[d]
    mzdata = "%.6f" % zero_z[d]
    msisodata = "%.6f" % zero_siso[d]
    x_zero.append(mxdata)
    y_zero.append(mydata)
    z_zero.append(mzdata)
    siso_zero.append(msisodata)

for d in range(len(neg_x)):
    nxdata = "%.6f" % neg_x[d]
    nydata = "%.6f" % neg_y[d]
    nzdata = "%.6f" % neg_z[d]
    nsisodata = "%.6f" % neg_siso[d]
    neg_x_loop.append(nxdata)
    neg_y_loop.append(nydata)
    neg_z_loop.append(nzdata)
    neg_siso_loop.append(nsisodata)


# write cube file
with open('unformartcube2.cube', 'w') as csvfile:
    cubewriter = csv.writer(csvfile, delimiter='\t',
                            quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    for nc in range(len(siso_zero)):
        cubewriter.writerow([x_zero[nc], y_zero[nc], z_zero[nc], siso_zero[nc]])
    pass
    for c in range(len(siso)):
        cubewriter.writerow([x_loop[c], y_loop[c], z_loop[c], siso[c]])
    pass
    for c in range(len(neg_siso_loop)):
        cubewriter.writerow([neg_x_loop[c], neg_y_loop[c], neg_z_loop[c], neg_siso_loop[c]])
    pass
csvfile.close()
