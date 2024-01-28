from . import print_terms

def pick(list_terms, upper, lower):
    print(len(list_terms))
    final_terms=[]

    i=0
    a=0
    for item in upper:
        if list_terms[0].isi(item)==1:
            i=i+1
        elif list_terms[0].isa(item)==1:
            a=a+1
    up_list=[i,a]
    i=0
    a=0
    for item in lower:
        if list_terms[0].isi(item)==1:
            i=i+1
        elif list_terms[0].isa(item)==1:
            a=a+1
    lo_list=[i,a]
    print(' here is the pick function list in input', up_list, lo_list)
    for term in list_terms:
        flag=0
        up=[]
        lo=[]
        for op in term.st[0]:
            if op.kind=='op':
                i=0
                a=0
                for ind in op.upper:
                    if term.isi(ind)==1:
                        i=i+1
                    elif term.isa(ind)==1:
                        a=a+1
                up=[i,a]
                i=0
                a=0
                for ind in op.lower:
                    if term.isi(ind)==1:
                        i=i+1
                    elif term.isa(ind)==1:
                        a=a+1
                lo=[i,a]
                flag=1
        print(up, up_list, lo, lo_list)
        if up==up_list and lo==lo_list and flag==1:
            print('yes')
            final_terms.append(term)

    print(len(final_terms))
    return final_terms
                
                        
                
def pick_test(list_terms, upper, lower):
    print(len(list_terms))
    final_terms=[]

    i=0
    a=0
    for item in upper:
        if list_terms[0].isi(item)==1:
            i=i+1
        elif list_terms[0].isa(item)==1:
            a=a+1
    up_list=[i,a]
    i=0
    a=0
    for item in lower:
        if list_terms[0].isi(item)==1:
            i=i+1
        elif list_terms[0].isa(item)==1:
            a=a+1
    lo_list=[i,a]
    print(' here is the pick function list in input', up_list[0],up_list[1], lo_list)
    for term in list_terms:
        flag=0
        up=[]
        lo=[]
        for op in term.st[0]:
            if op.kind=='op' and len(op.upper)==len(upper):
                i=0
                a=0
                pu=0
                for ind in op.upper:
                    if term.isi(ind)==1:
                        i=i+1
                    elif term.isa(ind)==1:
                        a=a+1

                    elif term.isp(ind)==1:
                        pu=pu+1
                up=[i,a]
                i=0
                a=0
                pl=0
                for ind in op.lower:
                    if term.isi(ind)==1:
                        i=i+1
                    elif term.isa(ind)==1:
                        a=a+1
                    elif term.isp(ind)==1:
                        pl=pl+1
                lo=[i,a]
                flag=1
        print(up, up_list, lo, lo_list, flag)
        


        if up==up_list and lo==lo_list and flag==1:
            print('yes')
            final_terms.append(term)
         
        elif pu!=0 or pl!=0:
            if pu!=0 and flag==1:

                for u in range(pu+1):
                    up1=[]
                    up1=[up[0]+u,up[1]+pu-u]
                    if up1==up_list and lo==lo_list:
                        print('yes')
                        final_terms.append(term)
            elif pl!=0 and flag==1:
                for l in range(pl+1):
                    lo1=[]
                    lo1=[lo[0]+l,lo[1]+pl-l]
                    if up==up_list and lo1==lo_list:
                        print('yes')
                        final_terms.append(term)
        elif pu!=0 and pl!=0 and flag==1:
            for u in range(pu+1):
                for l in range(pl+1):
                    up1=[]
                    lo1=[]
                    up1=[up[0]+u,up[1]+pu-u]
                    lo1=[lo[0]+l,lo[1]+pl-l]
                    if up1==up_list and lo1==lo_list:
                        print('yes')
                        final_terms.append(term)
    print(len(final_terms))
    return final_terms
                
                        
                
