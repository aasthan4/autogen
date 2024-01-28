import copy
from . import class_term
from . import compare_functions as cf
import numpy as np

def permute_matrix_check(term1,term2,after_permute):
    #limit to case of two sets of equivalent operators (3rd order comm)
    #print 'after_permute matrix',after_permute
    for op in after_permute:
        for set_p in op:
            imat=np.copy(term2.imatrix)
            amat=np.copy(term2.amatrix)
            tmp_set=copy.copy(set_p)

            #print 'imat before exchange', imat
            for i in range(len(tmp_set)):
                for j in range(i+1,len(tmp_set)):
                    if tmp_set[i]>tmp_set[j]:
                        imat[[set_p[i],set_p[j]]]=imat[[set_p[j],set_p[i]]]
                        imat[:,[set_p[i],set_p[j]]]=imat[:,[set_p[j],set_p[i]]]
                        amat[[set_p[i],set_p[j]]]=amat[[set_p[j],set_p[i]]]
                        amat[:,[set_p[i],set_p[j]]]=amat[:,[set_p[j],set_p[i]]]

                        tmp_op=term2.large_op_list[tmp_set[i]]
                        term2.large_op_list[tmp_set[i]]=term2.large_op_list[tmp_set[j]]
                        term2.large_op_list[tmp_set[j]]=tmp_op

                        tmp_coeff=term2.coeff_list[tmp_set[i]]
                        term2.coeff_list[tmp_set[i]]=term2.coeff_list[tmp_set[j]]
                        term2.coeff_list[tmp_set[j]]=tmp_coeff

                        tmp=tmp_set[i]
                        tmp_set[i]=tmp_set[j]
                        tmp_set[j]=tmp


                        term2.imatrix=copy.copy(imat)
                        term2.amatrix=copy.copy(amat)
            #print imat
            #print 'imat after exchange', imat
            if np.array_equal(imat,term1.imatrix) and np.array_equal(amat,term1.amatrix):
                if cf.permutation_check(term1,term2):
                    #print 'this matrix was found equal:',term1.coeff_list,term2.coeff_list,term1.imatrix,imat,after_permute
                    return term1,term2,1
    return term1,term2,0 

def positionchange(term1, term2):
    #for each name of operator in term1, if op in the same place if of different type
    first=-1
    second=-1
    #print 'compare operators', term1.large_op_list, term2.large_op_list
    for i in range(len(term1.large_op_list)):
        if term1.large_op_list[i].name[0]!=term2.large_op_list[i].name[0] or term1.large_op_list[i].name[1]!=term2.large_op_list[i].name[1]:
            first=i
            #print 'first position is ',first
    if first!=-1:
        for i in range(len(term1.large_op_list)):
            if term1.large_op_list[i].name[0]!=term2.large_op_list[i].name[0] or term1.large_op_list[i].name[1]!=term2.large_op_list[i].name[1]:

                if first!=i:
                    second=i
                    #print 'second pos is', second
    if second!=-1 and first!=-1:
        return permute_matrix_check(term1,term2,[[[first,second]]])
        
    #find second position of same type of op and exchange
    return term1,term2,0
