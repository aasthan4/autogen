import copy
import print_terms as pt
import compare_overall2 as ce
import full_con
def calrank(term,oplist):

    coefflist=[]
    rank=0
    for z in oplist:
        coefflist.append(term.coeff_list[z])
    for coeff in coefflist:
        for i in range(len(coeff)):
            dummy=0
            for coeff2 in coefflist:
                if coeff[i] in coeff2 and coeff2!=coeff:
                    dummy=1
            if dummy==0 and term.isi(coeff[i]):
                if (i<(len(coeff)/2)):

                    #print 'rank -'
                    rank=rank-0.5
                else:
                    #print 'rank +'
                    rank=rank+0.5
            elif dummy==0 and term.isa(coeff[i]):
                if (i<(len(coeff)/2)):
                    #print 'rank +'
                    rank=rank+0.5
                else:
                    #print 'rank -'
                    rank=rank-0.5
        print 'rank', rank
    return rank
def present(l, coefflist):
    flag=0
    for coeff in coefflist:
        for c in coeff:
            if c==l:
                flag=flag+1

    if flag==1:
        return 0
    elif flag==2 :
        return 1
    else:
        print 'l not found in preseent'
        exit()
def issingleex(term,oplist):

    coefflist=[]
    for z in oplist:
        coefflist.append(term.coeff_list[z])
    a=0
    i=0
    for coeff in coefflist:
        for c in coeff:
            if term.isi(c) and not present(c,coefflist):
                i=i+1
            elif term.isa(c) and not present(c,coefflist):
                a=a+1
    if i==1 and a==1:
        print coefflist
        return 1
    else:
        return 0
def isdoubleex(term,oplist,rank):
    coefflist=[]
    for z in oplist:
        coefflist.append(term.coeff_list[z])
    i=0
    a=0
    for coeff in coefflist:
        for c in coeff:
            if term.isi(c) and not present(c,coefflist):
                i=i+1
            elif term.isa(c) and not present(c,coefflist):
                a=a+1
    if i==2 and a==2 and abs(rank)==2:

        return 1
    else:
        return 0


def select(list_terms,arg,fac):
    list_terms_tmp=copy.deepcopy(list_terms)
    for term in list_terms_tmp:
        oplist=[]
        term.fac=term.fac*fac
        for i in arg:
            flag=0

            print 'this is the operation arg',i
            for op in range(len(term.large_op_list)):
                print 'flag,op name , len', flag,term.large_op_list[op].name,len(oplist)
                if len(oplist)==0:
                    if term.large_op_list[op].name[0]=='V':
                        print 'appended this in oplist',term.large_op_list[op].name
                        oplist.append(op)
                        flag=1
                        break
                #VT22T11
                elif term.large_op_list[op].name[0]!='V' and term.large_op_list[op].name[0]!='X': 


                    if int(term.large_op_list[op].name[2])==len(oplist):

                        print 'appended this in oplist',term.large_op_list[op].name
                        oplist.append(op)
                        flag=1
                        break
            if flag==0:
                print 'ERROR: flag=0 in h_third function'
                exit()
            print 'for rank in ', oplist
            rank=calrank(term,oplist)
            singleex=0
            #is the resulting operator a single excitation:
            singleex=issingleex(term,oplist)
            doubleex=isdoubleex(term,oplist,rank)
            if doubleex or singleex:
                print 'this term is n------', singleex, doubleex
            if i=='n':
                if not doubleex and not singleex:
                    term.fac=0.0
                    print 'deleted one term'

            elif i=='r':
                if doubleex or singleex:
                    term.fac=0.0
                    print 'deleted one term'

    list_terms_tmp=pt.clean_list(list_terms_tmp)
    for item in list_terms:
        if item.fac!=0.0:
            print term.coeff_list

    return list_terms_tmp

def select_hthird(list_terms):
    list_terms1=[]
    list_terms=full_con.full_terms(list_terms)
    list_terms=pt.clean_list(list_terms)
    list_terms1=select(list_terms,['n','a','r','a'],1.0/24.0)
    list_terms1.extend(select(list_terms,['n','r','a','a'],-1.0/24.0))
    list_terms1.extend(select(list_terms,['n','r','r','a'],1.0))
    list_terms1.extend(select(list_terms,['r','r','r','a'],1.0/4.0))
    list_terms1.extend(select(list_terms,['r','r','a','a'],-1.0/12.0))

    #list_terms=ce.compare_envelope(list_terms1,1.0,1.0)
    return list_terms1
        
        


