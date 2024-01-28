import copy
from library.compare_test import create_matrices

def no_connection(term,oplist,twice):
    coeff_list=[]
    for i in oplist:
        newcoeff=copy.deepcopy(term.coeff_list[i])
        flag=0
        for j in newcoeff:
            if coeff_list:
                for coeff in coeff_list:
                    #print 'this is what is being compared in no_connection', j, coeff
                    if j in coeff:
                        flag=1
                        break
            else:
                flag=1
        #only if the operator not connected is not a equivalent operator such as T1 in VT1T1T2
        if flag==0 and i not in twice:
            return 1
        coeff_list.append(copy.deepcopy(newcoeff))
    return 0
def not_connected(term,twice):
    oplist=[]
    flag=0
    #print 'this term is ', term.coeff_list,'\n'
    for i in range(len(term.large_op_list)-1):
        for op in range(len(term.large_op_list)):
            #print 'flag,op name , len', flag,term.large_op_list[op].name,len(oplist)
            if len(oplist)==0:
                if term.large_op_list[op].name[0]=='V':
                    #print 'appended this in oplist',term.large_op_list[op].name
                    oplist.append(op)
                    flag=1
                    break
            #VT22T11
            elif term.large_op_list[op].name[0]!='V' and term.large_op_list[op].name[0]!='X': 
                if int(term.large_op_list[op].name[2])==len(oplist):
                    #print 'appended this in oplist',term.large_op_list[op].name
                    oplist.append(op)
                    flag=1
                    break
        if flag==0:
            print('ERROR: flag=0 in h_thrid function while adding permutation of same terms')
            exit()
    #print 'oplist and no_connection', oplist,no_connection(term,oplist)
    return no_connection(term,oplist,twice)

def sameoperatorcase_addterms(list_terms):
    #Case VT1T1T2. T1 and T1' arre two same type of operators. if operators are not same they are already permuted in cases of commutator.
    #Problem: One of the cases, where one of the operators contracts first and the other does second might not arrise in this
    #...This commutator does not see the permutation of these two operators and will add both order of contractions to a 
    #...single term. 
    #solution: make another term with different permutation and half of the factor
    list_terms_add=[]
    for term in list_terms:
        #see if an operator arises twice
        equiv=0
        for i in range(1,len(term.large_op_list)):

            if equiv==0:
                twice=[]
                twice.append(i)
                for j in range(i+1,len(term.large_op_list)):
                    if term.large_op_list[i].name[0]==term.large_op_list[j].name[0] and int(term.large_op_list[i].name[1])==int(term.large_op_list[j].name[1]):
                        twice.append(j)
                        equiv=equiv+1
        if equiv==1:
            term.fac=term.fac/2.0
            tmp_term=copy.deepcopy(term)
            temp=copy.deepcopy(tmp_term.coeff_list[twice[0]])
            tmp_term.coeff_list[twice[0]]=copy.deepcopy(tmp_term.coeff_list[twice[1]])
            tmp_term.coeff_list[twice[1]]=temp
            #test if new term is possible (only check for interchangable operators. different operators are checked in different commutators.)
            if not_connected(tmp_term,twice)==1:
                tmp_term.fac=0.0
                #term.fac=term.fac*2.0
            else:
                #print 'new term generated', term.coeff_list,tmp_term.coeff_list,'notconnection',not_connected(tmp_term,twice)
                list_terms_add.append(copy.deepcopy(tmp_term))

        if equiv==2:
            term.fac=term.fac/6.0

            tmp_term1=copy.deepcopy(term)
            tmp_term2=copy.deepcopy(term)
            tmp_term3=copy.deepcopy(term)
            tmp_term4=copy.deepcopy(term)
            tmp_term5=copy.deepcopy(term)

            temp=copy.deepcopy(tmp_term1.coeff_list[twice[0]])#213
            tmp_term1.coeff_list[twice[0]]=copy.deepcopy(tmp_term.coeff_list[twice[1]])
            tmp_term1.coeff_list[twice[1]]=temp
            temp=copy.deepcopy(tmp_term2.coeff_list[twice[0]])#321
            tmp_term2.coeff_list[twice[0]]=copy.deepcopy(tmp_term.coeff_list[twice[1]])
            tmp_term2.coeff_list[twice[2]]=temp
            temp=copy.deepcopy(tmp_term3.coeff_list[twice[0]])#132
            tmp_term3.coeff_list[twice[1]]=copy.deepcopy(tmp_term.coeff_list[twice[1]])
            tmp_term3.coeff_list[twice[2]]=temp
            temp=copy.deepcopy(tmp_term4.coeff_list[twice[0]])#231
            tmp_term4.coeff_list[twice[0]]=copy.deepcopy(tmp_term.coeff_list[twice[1]])
            tmp_term4.coeff_list[twice[1]]=copy.deepcopy(tmp_term.coeff_list[twice[2]])
            tmp_term4.coeff_list[twice[2]]=temp
            temp=copy.deepcopy(tmp_term5.coeff_list[twice[0]])#312
            tmp_term5.coeff_list[twice[0]]=copy.deepcopy(tmp_term.coeff_list[twice[2]])
            tmp_term5.coeff_list[twice[2]]=copy.deepcopy(tmp_term.coeff_list[twice[1]])
            tmp_term5.coeff_list[twice[1]]=temp

            list_terms_add.append(copy.deepcopy(tmp_term1))
            list_terms_add.append(copy.deepcopy(tmp_term2))
            list_terms_add.append(copy.deepcopy(tmp_term3))
            list_terms_add.append(copy.deepcopy(tmp_term4))
            list_terms_add.append(copy.deepcopy(tmp_term5))

            #print 'length ',len(list_terms_add)
            #for term in list_terms_add:
            #    print term.coeff_list
            #exit()

    list_terms.extend(list_terms_add)
    for term in list_terms:
        create_matrices(term)
    return list_terms



