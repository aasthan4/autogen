import copy
from . import class_pos as pos 
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

        print('not returning in givepos in level 5 compare')
        return 0
    #print pos.i1,pos.i2,order 
    print("partner from function-give-pos :",coeff[pos.i1][pos.i2],"order",order)
    return pos
#****pickk funtion
#**input coeff_list1 and 2, order of picking i.e in {a,b,c,d}
#****Order 1- a,a 2-a,b, 3- b,a 4-b,b
# algo -
#***for loop on coefficients of one
#***is not all index seen in this coeff, pick based on order
#***add to seen list. 
#****NOTE : do add the picked objects to seen_list outside the pick call
def coeff_allseen(term,coeff,seen_list):
    flag=1
    post=pos.pos(0,0)
    j=term.coeff_list.index(coeff)
    for i in range(len(coeff)):
        post.i1=j
        post.i2=i
        if post not in seen_list:
            flag=0
    return flag
def pick(sign,term1,term2,seen_list1,seen_list2,order):
    pos1=pos.pos(-1,-1)
    pos2=pos.pos(-1,-1)
    for i in range(len(term1.coeff_list)):
        if order!=0:

            if len(term1.coeff_list[i])==4 and coeff_allseen(term1,term1.coeff_list[i],seen_list1)==0 and coeff_allseen(term2,term2.coeff_list[i],seen_list2)==0 :
                if order==1:
                    pos1.i1=i
                    pos1.i2=0
                    pos2.i1=i
                    pos2.i2=0
                    if seen(seen_list,pos1)==0 and seen(seen_list,pos2):
                        return pos1,pos2
                elif order==4:
                    pos1.i1=i
                    pos1.i2=1
                    pos2.i1=i
                    pos2.i2=1
                    if seen(seen_list,pos1)==0 and seen(seen_list,pos2)==0:
                        return pos1,pos2
                    else :
                        print("both options in order 1 are seen (function pick in compare)")
                        return pos1,pos2
                elif order==2:
                    pos1.i1=i
                    pos1.i2=0
                    pos2.i1=i
                    pos2.i2=1
                    if seen(seen_list,pos1)==0 and seen(seen_list,pos2):
                        return pos1,pos2
                elif order==3:
                    pos1.i1=i
                    pos1.i2=1
                    pos2.i1=i
                    pos2.i2=0
                    if seen(seen_list,pos1)==0 and seen(seen_list,pos2)==0:
                        return pos1,pos2
                    else :
                        print("both options in order 1 are seen (function pick in compare)")
                        return pos1,pos2
                else:
                    print("order unknown in pick in compare function")
                    exit()
            elif len(term1.coeff_list[i])==2 and coeff_allseen(term1,term1.coeff_list[i],seen_list1)==0 and coeff_allseen(term2,term2.coeff_list[i],seen_list2)==0:
                pos1.i1=i
                pos1.i2=0
                pos2.i1=i
                pos2.i2=0
                return pos1,pos2
