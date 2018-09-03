import copy
import time
import class_term
import functions
def pick(sign, term2, seen_list):
    #start from leftmost, pick leftmost unseen from daggered part
    if all_seen(seen_list)!=1
        for coeff in term2:
            for c in coeff:
                if len(c)==4:
                    pos[0]=index(coeff,term2)
                    pos[1]=0
                    if seen(seen_list,pos)==0:
                        return pos
                    else: 
                        pos[1]=1
                        if seen(seen_list,pos)==0:
                            return pos
                elif len(c)=2:
                    pos[0]=index(coeff,term2)
                    pos[1]=0
                    if seen(seen_list,pos)==0:
                        return pos
        print "ERROR compare level 5: Passed full unseen term, but cant find a dagger to pick"
    else :
        print "ERROR : trying to pick when all the term is seen"
        return 0
                    
def seen(seen_list, pos):
    if pos in seen_list:
        return 1
    else :
        return 0
#THIS FUNCTION IS NOT DESIGNED FOR TRIPLES
def to_partner(sign, seen_list, pos):
    #if pos is 1,2 return 3,4, make 1,2 seen
    #if pos is 1 return 2, make 1 seen
    #partner should not be already seen else eliminate
    #if match go find else return 0
def go_find(sign, term2, seen_list, pos2):
    #find ind in whole term and return position
    if not seen:
        #if match to partner
        #else:
        #return 0
def match(pos1,pos2,term1,term2,seel_list):
    #if ind1 and ind2 are of the same type
    #if ind2is not in seen list add to the list else think
def arrowwork(term1,term2,coeff1,coeff2):
    #1.pick in term1 and term2
    seen_list1=[]
    seen_list2=[]
    sign=1
    while all_seen(term2,
    pos1=pick(1, term1, seen_list1)
    pos2=pick(sign, term1, seen_list1)
    #2.if match ==1
    #3.to_partner
    #4.pick if 2 body and unseen only term2
    #5.if match==1
    #6.to_partner
def level5(term1,term2,final_terms):
    if arrowwork(term1,term2,coeff1,coeff2)==1:
        flag=term2.fac
    return flag
