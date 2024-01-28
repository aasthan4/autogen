def full_terms(list_terms):
    final_terms=[]
    for term in list_terms:
        if term.st[0][-1].kind!='op':
            final_terms.append(term)
    return final_terms
def full_con(st, co):
    final_t=[]
    final_co=[]
    for term, const in zip(st,co):
        flag=0
        for op in term:
            if op.kind=='op':
                flag=1
        if flag==0:
            final_t.append(term)
            final_co.append(const)
    return final_t, final_co
