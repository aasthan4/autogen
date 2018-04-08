def pick(list_terms, upper, lower):
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

    for term in list_terms:

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
	#print up, up_list
	if up==up_list and lo==lo_list:
	    final_terms.append(term)
    return final_terms
		
			
		
