def read_csv(MAXCOLS, filename):

    import csv

    data = []
    cols = [[] for _ in range(MAXCOLS)]

    with open(filename, 'r') as f:
        for row in csv.reader(f, delimiter=' '):
            for i in range(MAXCOLS):
                cols[i].append(row[i] if i < len(row) else '')

    x = list(map(float, cols[0]))
    y = list(map(float, cols[1]))
    z = list(map(float, cols[2]))
    iso = list(map(float, cols[3]))

    for i in range(len(x)):
        data.append([x[i], y[i], z[i], iso[i]])
    print(data[0])

    return data


# ori-layer, axis-layer, surface-layer, core-layer
def di_layers(data):

    ori = []
    axis_x = []
    axis_y = []
    axis_z = []
    surface_xz = []
    surface_yz = []
    surface_xy = []
    core = []

    for d in range(len(data)):
        # ori-layer
        if data[d][0] == 0.0 and data[d][1] == 0.0 and data[d][2] == 0.0:
            ori.append(data[d])

        # axis_x-layer
        if data[d][1] == 0.0 and data[d][2] == 0.0 and data[d][0] != 0.0:
            axis_x.append(data[d])

        # axis_y-layer
        if data[d][0] == 0.0 and data[d][2] == 0.0 and data[d][1] != 0.0:
            axis_y.append(data[d])

        # axis_z-layer
        if data[d][0] == 0.0 and data[d][1] == 0.0 and data[d][2] != 0.0:
            axis_z.append(data[d])

        # surface_xz-layer
        if data[d][1] == 0.0 and (data[d][0] != 0.0 and data[d][2] != 0.0):
            surface_xz.append(data[d])

        # surface_yz-layer
        if data[d][0] == 0.0 and (data[d][1] != 0.0 and data[d][2] != 0.0):
            surface_yz.append(data[d])

        # surface_xy-layer
        if data[d][2] == 0.0 and (data[d][0] != 0.0 and data[d][1] != 0.0):
            surface_xy.append(data[d])

        # core-layer
        if data[d][0] != 0.0 and data[d][1] != 0.0 and data[d][2] != 0.0:
            core.append(data[d])

    return len(ori), \
           len(axis_x), len(axis_y), len(axis_z), \
           len(surface_xz), len(surface_yz), len(surface_xy), \
           len(core)


def reflect_c1d(axis):

# -----------------------------main------------------------------- #
print(di_layers(read_csv(4, 'reflection-mp2.csv')))

