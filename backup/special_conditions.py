def startequiv_cond(list_terms):
    for term in list_terms:
        print  term.map_org 
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
        if t2>1:
            equivop='T2'
            first=0
            second=0
            for op in term.map_org:
                if equivop in op.name and 'Z' in op.name:
                    first=1
                elif equivop in op.name:
                    second=1
            #atleast 2 equivalent operators present with one of them as the first contraction.
            #If one of them has no connections with V, multiply with two.
            if first==1 and second==1:
                map_org=[]
                mapping=[]
                for item in term.large_op_list:
                    if equivop in item.name:
                        map_org.append(item)
                    if 'V2' in item.name or 'F1' in item.name:
                        ind=term.large_op_list.index(item)
                for item in term.coeff_list[ind]:
                    mapping.append(term.dict_ind[item])
                for item in map_org:
                    if item.name not in mapping:
                        term.fac=term.fac*2.0
        if d1>1:
            print 'inside the special conditions'
            equivop='D1'
            first=0
            second=0
            for op in term.map_org:
                if equivop in op.name and 'Z' in op.name:
                    first=1
                elif equivop in op.name:
                    second=1
            #atleast 2 equivalent operators present with one of them as the first contraction.
            #If one of them has no connections with V, multiply with two.
            if first==1 and second==1:
                map_org=[]
                mapping=[]
                for item in term.large_op_list:
                    if equivop in item.name:
                        map_org.append(item)
                    if 'V2' in item.name or 'F1' in item.name:
                        ind=term.large_op_list.index(item)
                for item in term.coeff_list[ind]:
                    mapping.append(term.dict_ind[item])
                for item in map_org:
                    if item.name not in mapping:
                        term.fac=term.fac*2.0
        if d2>1:
            equivop='D2'
            first=0
            second=0
            for op in term.map_org:
                if equivop in op.name and 'Z' in op.name:
                    first=1
                elif equivop in op.name:
                    second=1
            #atleast 2 equivalent operators present with one of them as the first contraction.
            #If one of them has no connections with V, multiply with two.
            if first==1 and second==1:
                map_org=[]
                mapping=[]
                for item in term.large_op_list:
                    if equivop in item.name:
                        map_org.append(item)
                    if 'V2' in item.name or 'F1' in item.name:
                        ind=term.large_op_list.index(item)
                for item in term.coeff_list[ind]:
                    mapping.append(term.dict_ind[item])
                for item in map_org:
                    if item.name not in mapping:
                        term.fac=term.fac*2.0
        if t1>1:
            equivop='T1'
            first=0
            second=0
            for op in term.map_org:
                if equivop in op.name and 'Z' in op.name:
                    first=1
                elif equivop in op.name:
                    second=1
            #atleast 2 equivalent operators present with one of them as the first contraction.
            #If one of them has no connections with V, multiply with two.
            if first==1 and second==1:
                map_org=[]
                mapping=[]
                for item in term.large_op_list:
                    if equivop in item.name:
                        map_org.append(item)
                    if 'V2' in item.name or 'F1' in item.name:
                        ind=term.large_op_list.index(item)
                for item in term.coeff_list[ind]:
                    mapping.append(term.dict_ind[item])
                for item in map_org:
                    if item.name not in mapping:
                        term.fac=term.fac*2.0
    return list_terms
