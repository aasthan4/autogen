'''
suggestion1: in case there is an error in sign function, do not use compare_overall2. instead use compare_overall in input file. It will not work with R,N functions.
'''
import numpy as np
import copy
from . import compare_functions as cf
from . import compare_functions2 as cf2
from .sign_function import level3_sign
def create_matrices(term):
    term.imatrix=np.zeros((len(term.large_op_list),len(term.large_op_list)))
    term.amatrix=np.zeros((len(term.large_op_list),len(term.large_op_list)))
    for i1 in range(len(term.large_op_list)):
        for i2 in range(i1+1,len(term.large_op_list)):
            for c1 in term.coeff_list[i1]:
                connect=0
                for c2 in term.coeff_list[i2]:
                    if c1==c2 and term.isi(c1)==1:
                        term.imatrix[i1][i2]+=1
                        term.imatrix[i2][i1]+=1
                    elif c1==c2 and term.isa(c1)==1:
                        term.amatrix[i1][i2]+=1
                        term.amatrix[i2][i1]+=1

    #print term.imatrix 
    #print term.amatrix 


def level1(term1,term2):
    #contractions made (E()() also of the same size)
    if len(term1.coeff_list)!=len(term2.coeff_list):
        return 0
    #all op in term1 in term2
    for item1 in term1.map_org:
        flag1=0
        for item2 in term2.map_org:
            if item1.name[0]==item2.name[0] and item1.name[1]==item2.name[1]:
                flag1=1
        if flag1!=1:
            return 0
    #all op in term2 in term1
    for item2 in term2.map_org:
        flag1=0
        for item1 in term1.map_org:
            if item1.name[0]==item2.name[0] and item1.name[1]==item2.name[1]:
                flag1=1
        if flag1!=1:
            return 0
    #uncontracted operator of same size
    if len(term1.st[0])!=len(term2.st[0]):
        return 0
    return 1


def compare(term1, term2):
    #print 'level1'
    flag=0
    #same operators and size of uncontracted part in both terms
    flag=level1(term1,term2)
    #print 'level 1 passed?', flag
    if flag==1:
        flag=0
        #print 'comparing two terms',term1.coeff_list, term2.coeff_list
        #simple case: contraction pattern identical in two terms
        if np.array_equal(term1.imatrix,term2.imatrix) and np.array_equal(term1.amatrix,term2.amatrix):
            if cf.permutation_check(term1,term2):
                #print 'the two terms are equal'#, term1.coeff_list, term2.coeff_list, term1.amatrix, term2.amatrix
                flag=1
            #else:
            #    #print 'two terms found are permutations'#,term1.coeff_list, term2.coeff_list
        else:
            #permutation case: contraction pattern of permuted operators compared
            #print 'terms are not equal', term1.coeff_list,term2.coeff_list
            #case when the position of type of operators is not the same VT1T2T1 VT2T1T1
            term1,term2,flag=cf2.positionchange(term1,term2)
            #print 'flag of position change', term1.coeff_list,term2.coeff_list,flag
            if flag!=1:
                #print 'permuting equivalent operators'
                term1,term2,flag=cf.level2(term1,term2)
    if flag==1:
        #print 'Starting to compute sign of equivalent term2'
        sign=level3_sign(term1,term2)
        #sign=1
        return 1.0
    return 0
