#import class_term
import copy
import numpy as np
def permutation_check(term1,term2):
    #checks if the two terms are two permutations on open indexes
    map1_open=[]
    map2_open=[]

    if 'X2' in term1.large_op_list[0].name:

        map1_open=[]
        for i in term1.coeff_list[0]:
            for j in range(1,len(term1.large_op_list)):
                for item in term1.coeff_list[j]:
                    if i==item:
                        map1_open.append(term1.large_op_list[j].name)
    if 'X2' in term2.large_op_list[0].name:
        map2_open=[]
        for i in term2.coeff_list[0]:
            for j in range(1,len(term2.large_op_list)):
                for item in term2.coeff_list[j]:
                    if i==item:
                        map2_open.append(term2.large_op_list[j].name)
    #case when two operators are eqivalent, create a new map for the two equivalent operators 
    #if the two maps are equal they are equivalent
    equal=1


    if map1_open and map2_open:
        #Two terms are permutations if the two terms are equal but the open indices are from different types of operators

        if map1_open[0][0]!=map2_open[0][0] or map1_open[0][1]!=map2_open[0][1]:
            equal=0
        if map1_open[1][0]!=map2_open[1][0] or map1_open[1][1]!=map2_open[1][1]:
            equal=0
        if map1_open[2][0]!=map2_open[2][0] or map1_open[2][1]!=map2_open[2][1]:
            equal=0
        if map1_open[3][0]!=map2_open[3][0] or map1_open[3][1]!=map2_open[3][1]:
            equal=0
        if equal==0:
            return 0
        #Now all types of operators are the same.


        
        eq12=1
        map1_op=[]
        map2_op=[]
        #case when the connections are to the same operator
        if map1_open==map2_open:
            return 1
        #Two terms are permutations when the two same type of operators are not equivalent
        if len(map1_open[0])>2 and len(map2_open[1])>2 :
            eq12=0
            print 'case indices',int(map1_open[0][2]),int(map2_open[0][2]),int(map1_open[1][2]),int(map2_open[1][2])
            if int(map1_open[0][2])!=int(map2_open[0][2]) and  int(map1_open[1][2])!=int(map2_open[1][2]):
                print 'entered case t11,t12'
                #check is the two opertors are equivalent
                for i in range(1,len(term1.large_op_list)):
                    if map1_open[0]==term1.large_op_list[i].name:
                        for c in term1.coeff_list[i]:
                            for j in range(len(term1.large_op_list)):
                                for d in term1.coeff_list[j]:
                                    if d==c and term1.large_op_list[j].name!=map1_open[0]:
                                        map1_op.append(term1.large_op_list[j].name)
                for i in range(1,len(term2.large_op_list)):
                    if map2_open[0]==term2.large_op_list[i].name:
                        for c in term2.coeff_list[i]:
                            for j in range(len(term2.large_op_list)):
                                for d in term2.coeff_list[j]:
                                    if d==c and term2.large_op_list[j].name!=map2_open[0]:
                                        map2_op.append(term2.large_op_list[j].name)
                #perutation also required to check two operators
                if map1_op and map2_op:
                    if map1_op==map2_op:
                        eq12=1
        eq34=1
        map3_op=[]
        map4_op=[]
        if len(map1_open[2])>2 and len(map2_open[3])>2 :
            eq32=0
            if int(map1_open[2][2])!=int(map2_open[2][2]) and  int(map1_open[3][2])!=int(map2_open[3][2]):
                #check is the two opertors are equivalent
                for i in range(1,len(term1.large_op_list)):
                    if map1_open[2]==term1.large_op_list[i].name:
                        for c in term1.coeff_list[i]:
                            for j in range(len(term1.large_op_list)):
                                for d in term1.coeff_list[j]:
                                    if d==c and term1.large_op_list[j].name!=map1_open[2]:
                                        map3_op.append(term1.large_op_list[j].name)

                for i in range(1,len(term2.large_op_list)):
                    if map2_open[0]==term2.large_op_list[i].name:
                        for c in term2.coeff_list[i]:
                            for j in range(len(term2.large_op_list)):
                                for d in term2.coeff_list[j]:
                                    if d==c and term2.large_op_list[j].name!=map2_open[3]:
                                        map4_op.append(term2.large_op_list[j].name)
                #perutation also required to check two operators
                if map1_op and map2_op:
                    if map1_op==map2_op:
                        eq34=1
        print 'equal variables', eq12,eq34,map1_open,map2_open,map1_op,map2_op,map3_op,map4_op
        if eq12==1 and eq34==1:
            return 1
        else:
            return 0
        #if equal34==1 and eq34==1:
        #    return 0

    return 1
def permute_matrix_check(term1,term2,after_permute):
    #limit to case of two sets of equivalent operators (3rd order comm)
    for op in after_permute:
        for set_p in op:
            imat=np.copy(term2.imatrix)
            amat=np.copy(term2.amatrix)
            tmp_set=copy.copy(set_p)
            for i in range(len(tmp_set)):
                for j in range(i+1,len(tmp_set)):
                    if tmp_set[i]>tmp_set[j]:
                        imat[[set_p[i],set_p[j]]]=imat[[set_p[j],set_p[i]]]
                        imat[:,[set_p[i],set_p[j]]]=imat[:,[set_p[j],set_p[i]]]
                        amat[[set_p[i],set_p[j]]]=amat[[set_p[j],set_p[i]]]
                        amat[:,[set_p[i],set_p[j]]]=amat[:,[set_p[j],set_p[i]]]

                        tmp=tmp_set[i]
                        tmp_set[i]=tmp_set[j]
                        tmp_set[j]=tmp
            #print imat
            if np.array_equal(imat,term1.imatrix) and np.array_equal(amat,term1.amatrix):
                if permutation_check(term1,term2):
                    print 'this matrix was found equal:',term1.coeff_list,term2.coeff_list,term1.imatrix,imat,after_permute
                    tmp_set=copy.copy(set_p)
                    for i in range(len(tmp_set)):
                        for j in range(i+1,len(tmp_set)):
                            if tmp_set[i]>tmp_set[j]:
                                tmp_op=term2.large_op_list[tmp_set[i]]
                                term2.large_op_list[tmp_set[i]]=term2.large_op_list[tmp_set[j]]
                                term2.large_op_list[tmp_set[j]]=tmp_op

                                tmp_coeff=term2.coeff_list[tmp_set[i]]
                                term2.coeff_list[tmp_set[i]]=term2.coeff_list[tmp_set[j]]
                                term2.coeff_list[tmp_set[j]]=tmp_coeff

                                tmp=tmp_set[i]
                                tmp_set[i]=tmp_set[j]
                                tmp_set[j]=tmp
                    return term1,term2,1
    return term1,term2,0 

def swap(a,b,c):
    tmp=[]
    tmp = a[c]
    a[c]=a[b]
    a[b]=tmp

def heapit(a, size, n,ret):
    if size==1:
        ret.append(copy.deepcopy(a))
        return a
    for i in range(size):
        heapit(a, size-1, n, ret)
        if ((size%2)==1):
            swap(a,0,size-1)
        else:
            swap(a,i,size-1)


    return ret

def level2(term1,term2):
    ret=[]
    permute=[]
    t1=[]
    for i in range(len(term2.large_op_list)):
        if term2.large_op_list[i].name[0]=='T' and term2.large_op_list[i].name[1]=='1':
            t1.append(i)
    t2=[]
    for i in range(len(term2.large_op_list)):
        if term2.large_op_list[i].name[0]=='T' and term2.large_op_list[i].name[1]=='2':
            t2.append(i)
    d1=[]
    for i in range(len(term2.large_op_list)):
        if term2.large_op_list[i].name[0]=='D' and term2.large_op_list[i].name[1]=='1':
            d1.append(i)
    d2=[]
    for i in range(len(term2.large_op_list)):
        if term2.large_op_list[i].name[0]=='D' and term2.large_op_list[i].name[1]=='2':
            d2.append(i)
    if len(t1)>1:
        permute.append(t1)
    if len(t2)>1:
        permute.append(t2)
    if len(d1)>1:
        permute.append(d1)
    if len(d2)>1:
        permute.append(d2)

    #crete all permutations of equivalent operator positions
    after_permute=[]
    for item in permute:
        after_permute.append(heapit(item, len(item), len(item),ret))
    #print 'the permute cordinates are:', after_permute
    #create all possible permuted matrices and compare by row and column interchange
    return permute_matrix_check(term1,term2,after_permute)
