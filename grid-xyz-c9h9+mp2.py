# nx = 70
# ny = 90
# nz = 70
# dalta = 0.05
# t = []
def GridGen(t):
    nx = 70
    ny = 90
    nz = 70
    dalta = 0.05
    t = []
    globals
    for x in range(-nx,nx+1,1):
        x = x * dalta
        for y in range(-ny,ny+1,1):
            y = y * dalta
            for z in range(-nz,nz+1,1):
                z = z * dalta
                t.append([x,y,z])
    print(t)
GridGen(3)
