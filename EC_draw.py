from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

def plot_ec(fn, bbox=(-3,3)):

    xmin, xmax, ymin, ymax, zmin, zmax = bbox*3
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    A = np.linspace(xmin, xmax, 100) 
    B = np.linspace(xmin, xmax, 50) 
    A1,A2 = np.meshgrid(A,A) 

    for z in B: 
        X,Y = A1,A2
        Z = fn(X,Y,z)
        cset = ax.contour(X, Y, Z+z, [z], zdir='z', alpha=0.2)
       
    for y in B: 
        X,Z = A1,A2
        Y = fn(X,y,Z)
        cset = ax.contour(X, Y+y, Z, [y], zdir='y', alpha=0.2)

    for x in B: 
        Y,Z = A1,A2
        X = fn(x,Y,Z)
        cset = ax.contour(X+x, Y, Z, [x], zdir='x', alpha=0.2)

    ax.set_zlim3d(zmin,zmax)
    ax.set_xlim3d(xmin,xmax)
    ax.set_ylim3d(ymin,ymax)

    plt.show()

def calc_points(A,b,p):
    Y = []
    X1r=[]
    X2r=[]
    Yr= []
    Points=(X1r,X2r,Yr)
    for i in range(p):
        Y.append(i**2)
    for x1 in range(p):
        for x2 in range(p):
            ys=(x1**3+x2**3+A[0]*x1+A[1]*x2+b)%p
            try:
                yr=Y.index(ys)
                X1r.append(x1)
                X2r.append(x2)
                Yr.append(yr)
                if yr!=0:
                    X1r.append(x1)
                    X2r.append(x2)
                    Yr.append(p-yr)
            except: 
                pass
    return Points

def plot_ec_on_ff(A,b,p):
    p=calc_points(A,b,p)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    cset = ax.scatter(p[0],p[1],p[2],marker='.',depthshade=True)
    plt.show()