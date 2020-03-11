import copy
import numpy
def countholes(term):
    holes=0
    for coeff in term.coeff_list:
        for item in coeff:
            if term.isi(item):
                holes++
    return holes
def level3_sign(term1,term2):
    print 'into sign function'
    sign1=0
    sign2=0
    holes1=countholes(term1)
    holes2=countholes(term2)
    loops1=countloops(term1)
    loops2=countloops(term2)
    if ((holes1+loops1)%2):
        sign1=-1
    else:
        sign1=+1
    if ((holes2+loops2)%2):
        sign2=-1
    else:
        sign2=+1
    if numpy.sign(term1.fac)==sign and numpy.sign(term2.fac)==sign2:

        if (term1.fac<0.0): 
            term1.fac=term1.fac - abs(term2.fac)
        else:
            term1.fac=term1.fac + abs(term2.fac)
        term1.fac=0.0
    elif numpy.sign(term1.fac)==sign and numpy.sign(term2.fac)!=sign2:

        if (term1.fac<0.0): 
            term1.fac=term1.fac + abs(term2.fac)
        else:
            term1.fac=term1.fac - abs(term2.fac)
        term1.fac=0.0
    elif numpy.sign(term1.fac)!=sign and numpy.sign(term2.fac)==sign2:
        if (term1.fac<0.0): 
            term1.fac=term1.fac + abs(term2.fac)
        else:
            term1.fac=term1.fac - abs(term2.fac)
        term1.fac=0.0 
    elif numpy.sign(term1.fac)!=sign and numpy.sign(term2.fac)!=sign2:
        if (term1.fac<0.0): 
            term1.fac=term1.fac - abs(term2.fac)
        else:
            term1.fac=term1.fac + abs(term2.fac)
        term1.fac=0.0 
    return 1
