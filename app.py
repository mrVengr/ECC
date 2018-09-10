import EC_draw as ec

def eliptic_curve(x,y,z):
    return x**3+y**3-x-y-z**2
# ec.plot_ec(eliptic_curve) # ec on field nєR 

ec.plot_ec_on_ff([-1,-1],0,7) # ec on finite field
