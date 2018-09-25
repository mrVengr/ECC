import EC_draw as ec

def eliptic_curve(x,y,z):
    return x**3+y**3-x-2*y+1-z**2
ec.plot_ec(eliptic_curve) # ec on field nєR 

ec.plot_ec_on_ff([-1,-2],1,17) # ec on finite field
#ec.plot_2D_ec(-1,1,7) # 2D ec

