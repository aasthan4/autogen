def create_map(term,equivop):
            #for op in term.map_org:
            #atleast 2 equivalent operators present with one of them as the first contraction.
            #If one of them has no connections with V, multiply with two.
            map_out=[]
            for op in term.large_op_list:
                if equivop in op.name:
                    mapping=[]
                    ind=term.large_op_list.index(op)#find the index of operator to work on coeff_list
                    for c in term.coeff_list[ind]:
                        found=0
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
def non_equivop(term,map_out,equivop):
    for i1 in range(len(map_out)):
        for i2 in range(len(map_out)):
            if i1!=i2:
                for item1 in map_out[i1]:
                    if item1 not in map_out[i2] and equivop not in item1:#different (closed) line in two operators. 
                        # note that an operator except H cannot contract with other of the same type.
                        #print 'found a unique connection'
                        #non equiv if the different line forms before the other equivop comes in  
                        pos1=1
                        pos2=1
                        for op in term.large_op_list:
                            if equivop in op.name and len(op.name)>2:
                                if op.name[2]>pos1:
                                    pos1=op.name[2]
                        if len(item1)>2:
                            pos2=item1[2]
                        if pos1>pos2:
                            return 1
    return 0
def startequiv_cond(list_terms):
    for term in list_terms:
        #print  term.map_org 
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
            if non_equivop(term,map_out,equivop):
                #print 'found nonequivalent operator case'
                term.fac=term.fac*2.0
        if d2>1:
            equivop='D2'
            map_out=create_map(term,equivop)
            if non_equivop(term,map_out,equivop):
                #print 'found nonequivalent operator case'
                term.fac=term.fac*2.0
        if t1>1:
            equivop='T1'
            map_out=create_map(term,equivop)
            if non_equivop(term,map_out,equivop):
                #print 'found nonequivalent operator case'
                term.fac=term.fac*2.0
        if t2>1:
            equivop='T2'
            map_out=create_map(term,equivop)
            if non_equivop(term,map_out,equivop):
                #print 'found nonequivalent operator case'
                term.fac=term.fac*2.0
    return list_terms
