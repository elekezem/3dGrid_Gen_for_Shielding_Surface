import csv


def read_csv(MAXCOLS, filename):

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

    return data


# divide origin data ori-layer, axis-layer, surface-layer, core-layer
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
    return ori, axis_x, axis_y, axis_z, surface_xz, surface_yz, surface_xy, core


def reflect_c1d(axis):
    for d in range(len(axis)):
        # for x axis
        if axis[d][0] != 0:
            axis.append([-axis[d][0], axis[d][1], axis[d][2], axis[d][3]])
        # for y axis
        elif axis[d][1] != 0:
            axis.append([axis[d][0], -axis[d][1], axis[d][2], axis[d][3]])
        # for z axis
        elif axis[d][2] != 0:
            axis.append([axis[d][0], axis[d][1], -axis[d][2], axis[d][3]])

    # print(len(axis))
    return axis


def reflect_c2d(surface):
    for d in range(len(surface)):
        # for yz surface
        if surface[d][0] == 0.0:
            surface.append([surface[d][0], -surface[d][1], -surface[d][2], surface[d][3]])
        # for xz surface
        elif surface[d][1] == 0.0:
            surface.append([-surface[d][0], surface[d][1], -surface[d][2], surface[d][3]])
        # for xy surface
        elif surface[d][2] == 0.0:
            surface.append([-surface[d][0], -surface[d][1], surface[d][2], surface[d][3]])

    # print(len(surface))
    return surface


def reflect_c3d(data):
    # 3 step
    for d in range(len(data)):
        # y reflection
        data.append([data[d][0], -data[d][1], data[d][2], data[d][3]])
        # z reflection
        data.append([data[d][0], data[d][1], -data[d][2], data[d][3]])
        # yz reflection
        data.append([data[d][0], -data[d][1], -data[d][2], data[d][3]])

    # print(len(data))
    return data


def reflect_d2d(reflect):
    for d in range(len(reflect)):
        reflect.append([-reflect[d][1], reflect[d][0], reflect[d][2], reflect[d][3]])
    #print(len(reflect))

    return reflect


def extend_core(data):

    half_core = di_layers(data)[1] + reflect_c2d(di_layers(data)[4]) + \
                reflect_c2d(di_layers(data)[6]) + reflect_c3d(di_layers(data)[7])
    #print(len(half_core))
    return half_core


def extend_surface(data):

    ref_surface = di_layers(data)[0] + reflect_c1d(di_layers(data)[2]) + \
                  reflect_c1d(di_layers(data)[3]) + reflect_c2d(reflect_c2d(di_layers(data)[5]))

    #print(len(ref_surface))
    return ref_surface

# -----------------------------main------------------------------- #
data_ori = read_csv(4, 'reflection-mp2.csv')
data_unsort = reflect_d2d(extend_core(data_ori)) + extend_surface(data_ori)

with open('unsortcube', 'w') as csvfile:
        cubewriter = csv.writer(csvfile, delimiter=',',
                            quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        for d in range(len(data_unsort)):
            cubewriter.writerow([data_unsort[d][0],data_unsort[d][1],data_unsort[d][2],data_unsort[d][3],])
        pass
csvfile.close()
