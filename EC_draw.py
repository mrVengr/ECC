from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

def plot_ec(fn, bbox=(-4,4)):

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
    Ys = []
    X1r=[]
    X2r=[]
    Yr= []
    Points=(X1r,X2r,Yr)
    count=0
    for i in range(p):
        Ys.append((i**2)%p)
    Y=np.array(Ys)
    for x1 in range(p):
        for x2 in range(p):
            yc=(x1**3+x2**3+A[0]*x1+A[1]*x2+b)%p
            yarr=np.where(Y==yc)[0]
            for i in yarr:
                count+=1
                X1r.append(x1)
                X2r.append(x2)
                Yr.append(i)
                print(x1,x2,i)
    return (Points,count)

def plot_ec_on_ff(A,b,p):
    f=calc_points(A,b,p)
    p=f[0]
    count=f[1]
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    cset = ax.scatter(p[0],p[1],p[2],marker='o',depthshade=True)
    plt.title(count)
    plt.show()

def plot_2D_ec(a,b,p):
    Ys =[]
    Xr=[]
    Yr=[]
    count=0
    for i in range(p):
        Ys.append((i**2)%p)
    Y=np.array(Ys)
    for x in range(p):
        yc=(x**3+a*x+b)%p
        yarr=np.where(Y==yc)[0]
        for i in yarr:
            count+=1
            Xr.append(x)
            Yr.append(i)
    plt.scatter(Xr,Yr,marker='.')
    plt.title(count)
    plt.show()