#Algorithm:
#This file has the subrooutine for a problem of doing contraction two operators at a time. 
#When there is a commutator of operators, there can be a reduced factor of the term.
#This can happen when there are two operators of the same kind and equivallent, but the commutator type contraction structure in this program
#does not count a part of the possible contractions. 
#The solution is based on two cases:
#1. Case1: when one of the two commutators do not have a connection with one operator with order (commutator number) less than the
#lower of the two equivalent operators.
#2. Case 2: when there are operators in the middle of the two equivalent operators, and any of those operators have a connection to an 
#operator with lower order which is not among the equivalent operators.
#If any of the case is truw, multiply the term with two corresponding to the missing part. 

def create_map(term,equivop):
            #for op in term.map_org:
            #atleast 2 equivalent operators present with one of them as the first contraction.
            map_out=[]
            for op in term.large_op_list:
                if equivop in op.name:
                    mapping=[]
                    ind=term.large_op_list.index(op)#find the index of operator to work on coeff_list
                    for c in term.coeff_list[ind]:
                        found=0
                        if len(term.coeff_list)==len(term.large_op_list)+1:
                            for i in range(len(term.coeff_list)-1):
                                for j in range(len(term.coeff_list[i])-1):
                                    if term.coeff_list[i][j]==c and i!=ind:
                                        mapping.append(term.large_op_list[i].name)
                                        found=1
                                        #print 'contraction found'
                                        break
                        else:
                            for i in range(len(term.coeff_list)):
                                for j in range(len(term.coeff_list[i])):
                                    if term.coeff_list[i][j]==c and i!=ind:
                                        mapping.append(term.large_op_list[i].name)
                                        found=1
                                        #print 'contraction found'
                                        break

                        if found==0:
                            #print 'open index'
                            mapping.append(op.name)
                    map_out.append(mapping)
            return map_out
def create_map2(term,equivop):
    posop1=1000
    posop2=1000
    for op in term.large_op_list:
        if equivop in op.name:
            if posop1>(len(term.large_op_list)+1):
                if len(op.name)>2:
                    posop1=int(op.name[2])
                else:
                    posop1=1
                    print('the operator name doesnt have a position in special condition')
                    exit()
            elif posop2>(len(term.large_op_list)+1):
                if len(op.name)>2:
                    posop2=int(op.name[2])
                else:
                   posop2=1
                   print('the operator name doesnt have a position in special condition')
                   exit()
    oplistmiddle=[]
    #print 'position of two equiv operators',posop1,posop2
    for op in term.large_op_list:
        if len(op.name)>2:
            if int(op.name[2])>posop1 and  int(op.name[2])<posop2:
               oplistmiddle.append(op.name)
            elif int(op.name[2])<posop1 and int(op.name[2])>posop2:
                oplistmiddle.append(op.name)
    output=[]
    for op in oplistmiddle:
        output.extend(create_map(term,op))
    return output,oplistmiddle


def non_equivop(term,map_out,equivop):
    pos1=10000 #stores position of the first occuring equivop
    found_pos=0
    #print 'map_out case1', map_out
    for op in term.large_op_list:
        if equivop in op.name:
            #print equivop, op.name
            if len(op.name)>2:
                #print 'op.name >2',op.name,pos1
                if int(op.name[2])<pos1:
                    #print op.name[2],pos1
                    pos1=int(op.name[2])
                    found_pos=1
            else:
                pos1=0
                #print op.name[2],pos1
                found_pos=1
    ##if each equiv op is connected to a arm which is created before pos1, it is equiv. is one of the arms in one is created after the first pos, it is non-eq
    for opeq in map_out:
        inner_comm=0
        for op1 in opeq:
            if len(op1)>2:#case when the opeartor can be in outer comm
                pos2=int(op1[2])
                if pos2<pos1:
                    inner_comm=1
            elif op1[0]=='V':
                inner_comm=1
        #print 'opeq',inner_comm,opeq
        if inner_comm==0:
            #print 'found non equivalent operators: one operator has both connection to outer comm'
            return 1
    return 0    
def non_equivop2(term,map_out2,equivop,opmiddle):
    #case2: if the there is one connection in the middle operator which is not an equivalent operator and has comm position less than middle operator, it returns 0
    #print 'inside two'
    for opi in range(len(map_out2)):
        for c in map_out2[opi]:

            #print c, opmiddle[opi]
            if len(c)>2 and len(opmiddle[opi])>2:
                if (int(c[2])<int(opmiddle[opi][2])) and (equivop not in c):
                    return 0
            else:
                return 0
        #if it connects to two equivalent operators its fine
        first=0
        for c in map_out2[opi]:
            if equivop in c and len(c)>2 and first==0:
                first=c[2]
            elif equivop in c and len(c)>2 and first!=0:
                if c[2]!=first:
                    return 0
    if not opmiddle:
        return 0

    return 1

def startequiv_cond(list_terms):
    #if list_terms:
    #    #print list_terms
    #else:
    #    print 'doesnt'
    #    return []
    for term in list_terms:
        #print  term.large_op_list
        d1=0
        t1=0
        d2=0
        t2=0
        #check if there are equivalent operators

        for op in term.large_op_list:
            if op.name[0]=='T' and op.name[1]=='1':
                t1+=1
            if op.name[0]=='D' and op.name[1]=='1':
                d1+=1
            if op.name[0]=='T' and op.name[1]=='2':
                t2+=1
            if op.name[0]=='D' and op.name[1]=='2':
                d2+=1
        if d1>1:
            equivop='D1'
            map_out=create_map(term,equivop)
            case1=0
            case2=0
            case1=non_equivop(term,map_out,equivop)
            map_out2,oplistmiddle=create_map2(term,equivop)
            case2=non_equivop2(term,map_out2,equivop,oplistmiddle)
            if case1==1.0 or case2==1.0:
                term.fac=term.fac*2.0
            
        if d2>1:
            equivop='D2'
            map_out=create_map(term,equivop)
            case1=0
            case2=0
            case1=non_equivop(term,map_out,equivop)
            map_out2,oplistmiddle=create_map2(term,equivop)
            case2=non_equivop2(term,map_out2,equivop,oplistmiddle)
            if case1==1.0 or case2==1.0:
                term.fac=term.fac*2.0
        if t1>1:
            equivop='T1'
            map_out=create_map(term,equivop)
            case1=0
            case2=0
            case1=non_equivop(term,map_out,equivop)
            map_out2,oplistmiddle=create_map2(term,equivop)
            case2=non_equivop2(term,map_out2,equivop,oplistmiddle)
            #print 'case 1 and 2', case1, case2
            if case1==1.0 or case2==1.0:
                #print 'special condition involked'
                term.fac=term.fac*2.0
        if t2>1:
            equivop='T2'
            map_out=create_map(term,equivop)
            case1=0
            case2=0
            case1=non_equivop(term,map_out,equivop)
            map_out2,oplistmiddle=create_map2(term,equivop)
            case2=non_equivop2(term,map_out2,equivop,oplistmiddle)
            if case1==1.0 or case2==1.0:

                term.fac=term.fac*2.0
    return list_terms
