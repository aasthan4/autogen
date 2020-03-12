import copy
import numpy
def countholes(term):
    holes=0
    seen2=[]
    for coeff in term.coeff_list:
        for item in coeff:
            if term.isi(item) and item not in seen2:
                seen2.append(item)
                holes=holes+1
    #print 'holes are',holes
    return holes
def find(op,i,term):
    for op2 in range(1,len(term.large_op_list)):
        for i2 in term.coeff_list[op2]:
            #print 'found i and op in find function', i2,i,op2,op
            if i==i2 and op2!=op:

                comb=[]
                comb.append(i2)
                comb.append(op2)
                #print 'returning comb'
                return comb
    print 'next operator not found for i and op name', i, term.large_op_list[op]
    exit()
    return []
def next_op(op,i,term):
    comb=[]
    #case 1: coeff with two indexes
    if len(term.coeff_list[op])==2:

        #print 'case1 in next op'
        if term.coeff_list[op][1]==i:

            comb=[]
            comb.append(term.coeff_list[op][0])
            comb.append(op)
            return comb
        else:
           return find(op,i,term)
    elif len(term.coeff_list[op])==4:
        #print 'case2 in next op',term.coeff_list[op],i
        if term.coeff_list[op][3]==i:
            comb=[]
            comb.append(term.coeff_list[op][1])
            comb.append(op)
            return comb
        if term.coeff_list[op][2]==i:
            comb=[]
            comb.append(term.coeff_list[op][0])
            comb.append(op)
            return comb
        if term.coeff_list[op][1]==i or term.coeff_list[op][0]:
            #print 'starting find function'
            return find(op,i,term)
    return comb
def countloops(term):
    seen=[]
    comb=[]
    loopcount=0
    #print term.sum_list, term.coeff_list

    for op in range(1,len(term.large_op_list)):
        for i in term.coeff_list[op]:
            if not term.is_dummy(i) and term.isi(i):
                comb=[]
                comb.append(i)
                comb.append(op)

                seen.append(comb)
                loopcomplete=0
                while (loopcomplete==0):
                    comb=next_op(comb[1],comb[0],term)
                    #print 'next operator returned is',comb
                    if comb not in seen:
                        seen.append(comb)
                    else:
                        print 'next operator already seen error:',seen
                        exit()
                    if not term.is_dummy(comb[0]) and term.isa(comb[0]):
                        loopcount=loopcount+1
                        loopcomplete=1
    for op in range(1,len(term.large_op_list)):
        for i in term.coeff_list[op]:
            comb=[]
            comb.append(i)
            comb.append(op)
            if comb not in seen:
                seen.append(comb)
                loopcomplete=0
                while (loopcomplete==0):
                    comb=next_op(comb[1],comb[0],term)
                    if comb in seen:
                        loopcount=loopcount+1
                        loopcomplete=1
                    else:
                        seen.append(comb)
    #print 'loopcount', loopcount
    return loopcount
def level3_sign(term1,term2):
    #print 'into sign function,term1,term2',term1.sum_list,term1.coeff_list
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
    #print 'sign 1 and sign 2', sign1, numpy.sign(term1.fac),sign2, numpy.sign(term2.fac)
    #exit()
    if numpy.sign(term1.fac)==sign1 and numpy.sign(term2.fac)==sign2:

        if (term1.fac<0.0): 
            term1.fac=term1.fac - abs(term2.fac)
        else:
            term1.fac=term1.fac + abs(term2.fac)
        term2.fac=0.0
    elif numpy.sign(term1.fac)==sign1 and numpy.sign(term2.fac)!=sign2:

        if (term1.fac<0.0): 
            term1.fac=term1.fac + abs(term2.fac)
        else:
            term1.fac=term1.fac - abs(term2.fac)
        term2.fac=0.0
    elif numpy.sign(term1.fac)!=sign1 and numpy.sign(term2.fac)==sign2:
        if (term1.fac<0.0): 
            term1.fac=term1.fac + abs(term2.fac)
        else:
            term1.fac=term1.fac - abs(term2.fac)
        term2.fac=0.0 
    elif numpy.sign(term1.fac)!=sign1 and numpy.sign(term2.fac)!=sign2:
        if (term1.fac<0.0): 
            term1.fac=term1.fac - abs(term2.fac)
        else:
            term1.fac=term1.fac + abs(term2.fac)
        term2.fac=0.0 
    return 1
