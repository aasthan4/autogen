import library
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
def full_con_terms(list_terms):
    for i in range(len(list_terms)):
	flag=0
	for item in list_terms[i].st[0]:
	    if item.kind=='op' and flag==0:
		list_terms[i].fac=0.0
		flag=1
    return list_terms
