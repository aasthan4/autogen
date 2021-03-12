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
        #print 'maps are', map1_open, map2_open
        
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
        '''
        if map1_open[0][0]!=map2_open[0][0] or map1_open[0][1]!=map2_open[0][1] or  map1_open[0][2]!=map2_open[0][2]:
            equal=0
        if map1_open[1][0]!=map2_open[1][0] or map1_open[1][1]!=map2_open[1][1] or  map1_open[1][2]!=map2_open[1][2]:
            equal=0
        if map1_open[2][0]!=map2_open[2][0] or map1_open[2][1]!=map2_open[2][1] or  map1_open[2][2]!=map2_open[2][2]:
            equal=0
        if map1_open[3][0]!=map2_open[3][0] or map1_open[3][1]!=map2_open[3][1] or  map1_open[3][2]!=map2_open[3][2]:
            equal=0
        if equal==0:
            return 0
        '''
        #Now all types of operators are the same.


        
        eq12=1
        #case when the connections are to the same operator or same operators with different names
        f=1
        if map1_open==map2_open:
            f=1
            #missing case when the name of operators are same but they are different operators. 
            if np.array_equal(term1.imatrix,term2.imatrix) and np.array_equal(term1.amatrix,term2.amatrix):
                f=0
                return 1
            else:
                f=1
                #print term1.imatrix,term2.imatrix,map1_open,map2_open
                #exit()
                #return 0
        elif f==1:#happens in all cases except when we return 1
            flag=1
            for i in range(len(map1_open)):
                if map1_open[i]!=map2_open[i]:
                    flag=0
                    for opi in range(len(term1.large_op_list)):
                        if term1.large_op_list[opi].name==map1_open[i]:
                            first=opi
                        if term2.large_op_list[opi].name==map2_open[i]:
                            second=opi

                    if np.array_equal(term1.imatrix[first,:],term2.imatrix[second,:]) and np.array_equal(term1.amatrix[first,:],term2.amatrix[second,:]):
                        #case when the name of index in op1 is not the same in op2:permutation
                        for item1 in term1.coeff_list[first]:
                            if item1 not in term1.sum_list:
                                if item1 not in term2.coeff_list[second]:
                                    return 0 #is a permutation:name of opeen index different in two eq operators

                        #print 'found a case of same oper with different names'
                        flag=1
            if flag==1:
                #print 'returning case of same operator different names'
                return 1
        #Two terms are permutations when the two same type of operators are not equivalent
        if len(map1_open[0])>2 and len(map2_open[1])>2 :
            eq12=0

            #print 'case indices12',int(map1_open[0][2]),int(map2_open[0][2]),int(map1_open[1][2]),int(map2_open[1][2])
            if int(map1_open[0][2])==int(map2_open[0][2]) and  int(map1_open[1][2])==int(map2_open[1][2]):
                eq12=1
            else:
                #check is the two opertors are equivalent
                for i in range(1,len(term1.large_op_list)):
                    if map1_open[0]==term1.large_op_list[i].name:
                        first=i
                    if map1_open[1]==term1.large_op_list[i].name:
                        second=i


                #print np.array_equal(term1.imatrix[first,:],term1.imatrix[second,:])
                #exit()


                if np.array_equal(term1.imatrix[first,:],term1.imatrix[second,:]) and np.array_equal(term1.amatrix[first,:],term1.amatrix[second,:]):
                    eq12=1
        eq34=1
        if len(map1_open[2])>2 and len(map2_open[3])>2 :
            eq34=0
            #print 'case indices34',int(map1_open[2][2]),int(map2_open[2][2]),int(map1_open[3][2]),int(map2_open[3][2])
            if int(map1_open[2][2])==int(map2_open[2][2]) and  int(map1_open[3][2])==int(map2_open[3][2]):
                eq34=1
            else:
                #check is the two opertors are equivalent
                for i in range(1,len(term1.large_op_list)):
                    if map1_open[2]==term1.large_op_list[i].name:
                        first=i
                    if map1_open[3]==term1.large_op_list[i].name:
                        second=i
                if np.array_equal(term1.imatrix[first,:],term1.imatrix[second,:]) and np.array_equal(term1.amatrix[first,:],term1.amatrix[second,:]):
                    eq34=1
        #print 'equal variables', eq12,eq34,map1_open,map2_open#,map1_op,map2_op,map3_op,map4_op
        if eq12==1 and eq34==1:
            #print 'return 1 in eq12 and eq34'
            return 1 
        else:
            return 0
        #if equal34==1 and eq34==1:
        #    return 0

    return 1

def permute_matrix_check(term1,term2,after_permute):
    #limit to case of two sets of equivalent operators (3rd order comm)
    #print 'after_permute matrix',after_permute
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
                    #print 'permuted matrices',imat,term1.imatrix
            if np.array_equal(imat,term1.imatrix) and np.array_equal(amat,term1.amatrix):
                #print 'same connection check'
                if permutation_check(term1,term2):
                    #print 'this matrix was found equal:',term1.coeff_list,term2.coeff_list,term1.imatrix,imat,after_permute
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
                #else:
                #    print 'found permutation in permute equivalent function'
                #    #exit()
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
    #print term2.large_op_list
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
