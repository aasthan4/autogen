import copy
#*****gives the position of the partner intex to the present. 
#****if fixed is on gives the direct partner else any of the below
#****order gives whether you want partner above the present index or below.
#******i.e whether you have the below line or above line in a<-i.
#givepos(coeff_list,pos,fixed or not,if not fixed then which position if not 0)
def give_pos(coeff,pos,fixed,order):
    if order<len(coeff[pos.i1])/2:

        if pos.i2>=len(coeff[pos.i1])/2:

            if fixed==1:
                pos.i2=pos.i2-len(coeff[pos.i1])/2
            else:
                #**creating partner positionwhen the partner has to be orderth in the down indexes
                if (pos.i2-len(coeff[pos.i1])/2-order)<0:
                    pos.i2=len(coeff[pos.i1])/2+(pos.i2-len(coeff[pos.i1])/2-order)
        else:
            if fixed==1:
                pos.i2=pos.i2+len(coeff[pos.i1])/2
            else:
                #**creating partner positionwhen the partner has to be orderth in the down indexes
                if (pos.i2+len(coeff[pos.i1])/2+order)>=len(coeff[pos.i1]):
                    pos.i2=(len(coeff[pos.i1])/2)+(pos.i2+len(coeff[pos.i1])/2+order)%len(coeff[pos.i1])
                else :
                    pos.i2=pos.i2+len(coeff[pos.i1])/2+order
                    
    else:

        print 'not returning in givepos in level 5 compare'
        return 0
    #print pos.i1,pos.i2,order 
    print "partner from function-give-pos :",coeff[pos.i1][pos.i2],"order",order
    return pos

