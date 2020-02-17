import copy
import time
import class_term
import functions
import function_small
import class_pos as pos
#class pos(object):
#    def __init__(self, i1, i2):
#        self.i1=i1
#        self.i2=i2

def pick(sign, term2, seen_list):
    #start from leftmost, pick leftmost unseen from daggered part
    #if all_seen(term2,seen_list)!=1
        pos1=pos.pos(0,0)
        for coeff in term2.coeff_list:
                if len(coeff)==4:
                    pos1.i1=term2.coeff_list.index(coeff)
                    pos1.i2=0
                    if seen(seen_list,pos1)==0:
                        #seen_list=seen_list+[pos1]
                        seen_list.append(pos1)
                        return pos1
                    else: 
                        pos1.i2=1
                        if seen(seen_list,pos1)==0:

                            seen_list.append(pos1)
                            #seen_list=seen_list+[pos1]
                            return pos1
                elif len(coeff)==2:
                    pos1.i1=term2.coeff_list.index(coeff)
                    pos1.i2=0
                    if seen(seen_list,pos1)==0:
                        seen_list.append(pos1)
                        #seen_list=seen_list+[pos1]
                        return pos1
def all_seen(term, seen_list):
    for coeff_list in term.coeff_list: 
        for coeff in coeff_list:
            flag=0
            for item in seen_list:
                if item.i1==term.coeff_list.index(coeff_list) and item.i2==coeff_list.index(coeff):
                    flag=1
            if flag==0:
                return 0
    return 1
def seen(seen_list, pos):
    for p in seen_list:
        if p.i1==pos.i1 and p.i2==pos.i2:
            return 1
    return 0

def go_find(sign,term1,term2,seen_list1,seen_list2,pos1,pos2):
    flag1=0
    flag2=0
    pos_tmp=pos.pos(0,0)
    #print "inside ifind"
    #print term1.coeff_list,pos1.i1,pos1.i2
    for coeff in term1.coeff_list:
        for c in coeff:
            if c==term1.coeff_list[pos1.i1][pos1.i2]:
                pos_tmp.i1=term1.coeff_list.index(coeff)
                pos_tmp.i2=coeff.index(c)
                if not seen(seen_list1,pos_tmp):
                    pos1=copy.deepcopy(pos_tmp)
                    flag1=1
                    #print 'inside gofind1 ', pos1.i1,pos1.i2
                
    #print term2.coeff_list,pos2.i1,pos2.i2
    for coeff in term2.coeff_list:
        for c in coeff:
            if c==term2.coeff_list[pos2.i1][pos2.i2]:
                pos_tmp.i1=term2.coeff_list.index(coeff)
                pos_tmp.i2=coeff.index(c)
                if not seen(seen_list2,pos_tmp):
                    flag2=1
                    pos2=copy.deepcopy(pos_tmp)
                    #print 'inside gofind2 ', pos1.i1,pos2.i1,pos2.i2
                    
    #print 'flag 1 and 2 should be 1 -', flag1,flag2


    if flag1==1 and flag2==1:
        if match(term1,term2,pos1,pos2) and not seen(seen_list1,pos1) and not seen(seen_list2,pos2):
            #print "done adding"
            seen_list1.append(pos1)
            seen_list2.append(pos2)
            print "found pos in string 1 ", term1.coeff_list[pos1.i1][pos1.i2]
            print "found pos in string 2 ", term2.coeff_list[pos2.i1][pos2.i2]
            #print 'go_find',print_seen(seen_list1)
            return to_partner(sign,term1,term2,copy.deepcopy(seen_list1),copy.deepcopy(seen_list2),copy.deepcopy(pos1),copy.deepcopy(pos2))

        else:
            #print print_seen(seen_list1)
            return [0],[0],0
    elif all_seen(term1,seen_list1) and all_seen(term2,seen_list2):
        print "found the all seen stage program should end"
        return seen_list1,seen_list2,sign
    elif flag1==0 and flag2==0:
        return seen_list1,seen_list2,sign
    else:
        #print"got the case when atleast one of the index seen but not all seen"
        return [0],[0],0
#THIS FUNCTION IS NOT DESIGNED FOR TRIPLES
def to_partner(sign,term1,term2,seen_list1,seen_list2,pos1,pos2):
    pos1a=copy.deepcopy(pos1)
    pos2a=copy.deepcopy(pos2)
    seen_list1a=copy.deepcopy(seen_list1)
    seen_list2a=copy.deepcopy(seen_list2)
    function_small.give_pos(term1.coeff_list,pos1a,1,0)
    function_small.give_pos(term2.coeff_list,pos2a,1,0)
    signorg=copy.copy(sign)#**if the first route return sign 0 the second path shoudl be given original sign
    if match(term1,term2,pos1a,pos2a) and not seen(seen_list1a,pos1a) and not seen(seen_list2a,pos2a):
        #print 'inside to partner =',pos1a.i1,pos1a.i2,pos2a.i1,pos2a.i2
        seen_list1a.append(pos1a)
        seen_list2a.append(pos2a)
        #print 'to_partner',print_seen(seen_list1a)
        seen_listc1,seen_listc2,sign= go_find(signorg,term1,term2,copy.deepcopy(seen_list1a),copy.deepcopy(seen_list2a),copy.deepcopy(pos1a),copy.deepcopy(pos2a))
        print "COMPLETED 1st run",sign,term1.coeff_list[pos1.i1][pos1.i2]
        #print_seen(seen_listc1)
        if sign!=0:
            return seen_listc1,seen_listc2,sign
    else:

        sign=0
    print "broke tree",term1.coeff_list[pos1.i1][pos1.i2],term2.coeff_list[pos2.i1][pos2.i2],sign
    if sign==0:#when could not find a match in the path of order = 1 sign will be 0

        #print "after sign change"
        pos1b=copy.deepcopy(pos1)
        pos2b=copy.deepcopy(pos2)

        seen_list1b=copy.deepcopy(seen_list1)
        seen_list2b=copy.deepcopy(seen_list2)
        function_small.give_pos(term1.coeff_list,pos1b,1,0)
        function_small.give_pos(term2.coeff_list,pos2b,0,1)
        signorg=signorg*(-1)

        if match(term1,term2,pos1b,pos2b) and not seen(seen_list1b,pos1b) and not seen(seen_list2b,pos2b):
            #print 'inside to partner =',pos1b.i1,pos1b.i2,pos2b.i1,pos2b.i2
            seen_list1b.append(pos1b)
            seen_list2b.append(pos2b)
            #print 'to_partner',print_seen(seen_list1b)
            seen_listc1,seen_listc2,sign= go_find(signorg,term1,term2,copy.deepcopy(seen_list1b),copy.deepcopy(seen_list2b),copy.deepcopy(pos1b),copy.deepcopy(pos2b))
            print "COMPLETED 2nd run",sign, term1.coeff_list[pos1.i1][pos1.i2]
            if sign!=0:
                return seen_listc1,seen_listc2,sign
        else:
            #return [0],[0],0
            sign=0
    if sign==0:
        return [0],[0],0
def match(term1,term2,pos1,pos2):
    #if ind1 and ind2 are of the same type
    if term1.type(term1.coeff_list[pos1.i1][pos1.i2])==term2.type(term2.coeff_list[pos2.i1][pos2.i2]):
        return 1
    else: 
        print "mismatch at ", pos1.i1,pos1.i2
        return 0
    #if ind2is not in seen list add to the list else think
def print_seen(seen_list):
    #if len(seen_list)<=5:
        for item in seen_list:
            print item.i1,item.i2
    #else:
        #exit()
def arrowwork(term1,term2,coeff1,coeff2):
    #1.pick in term1 and term2
    seen_list1=[]
    seen_list2=[]
    sign=1
    while all_seen(term1,seen_list1)==0 and sign !=0:
        print "inside arrowowrk"
        sign=1  #note : if sign is always 1 then no use right? debug
        #pos1=pick(1, term1, seen_list1)#appends in seen_list
        #pos2=pick(sign, term2, seen_list2)
        function_small.pick(sign,term1,term2,seen_list1,seen_list2,1)
        #2.if match ==1

        print "after pick",term1.coeff_list[pos1.i1][pos1.i2],term2.coeff_list[pos2.i1][pos2.i2]
        if match(term1,term2,pos1,pos2):
            seen_listc1,seen_listc2,sign=to_partner(sign,term1,term2,copy.deepcopy(seen_list1),copy.deepcopy(seen_list2),copy.deepcopy(pos1),copy.deepcopy(pos2))
            print "after the first loop",sign
            if sign!=0:
                seen_list1=seen_listc1
                seen_list2=seen_listc2
            #print pos1.i1,pos1.i2,complete
        if not all_seen(term1,seen_list1) and not all_seen(term2,seen_list2):
            pos1=pick(sign,term1,seen_list1,)
            pos2=pick(sign,term2,seen_list2)
            print "after pick 2",term1.coeff_list[pos1.i1][pos1.i2],term2.coeff_list[pos2.i1][pos2.i2]
            exit()
        #4.pick if 2 body and unseen only term2
        #5.if match==1
        #6.to_partner
    if sign!=0:
        print "MATCHED ", sign
def level5(term1,term2,final_terms):
    flag=0
    print "checking", term1.coeff_list 
    print term2.coeff_list
    if arrowwork(term1,term2,term1.coeff_list,term2.coeff_list)==1:
        flag=term2.fac
    #exit()
    return flag
