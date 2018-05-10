import copy
#make unique function
def unique(i1,i2,list_ind,term):
    if term.dict_ind[list_ind[i1]]!=term.dict_ind[list_ind[i2]]:
	return 1
    return 0
#make split_terms
def spli_term(term,i1,i2):
   for coeff in term.coeff_list:
	for ind in range(len(coeff)):
	    if coeff[ind]==i1:
		 coeff[ind]=i2
	    elif coeff[ind]==i2:
		coeff[ind]=i1
   return copy.deepcopy(term)
def symm(list_terms):
    for term in list_terms:
	#this task has to be done on each term on other term as well
	other_terms=[]
	list_ind=[]
	final_terms=[]
	other_terms.append(term)
	#make a list of ind for finding unie pairs
	print term.st[0][-1].upper, term.st[0][-1].lower
	for coeff in term.coeff_list:
	    for ind in coeff:
		if ind not in term.sum_list:
		    list_ind.append(ind)
	print list_ind
	#find unique pairs and split terms into two or multiple of twos
	for i1 in range(len(list_ind)):
	    for i2 in range(i1,len(list_ind)):
	        if unique(i1,i2,list_ind, term):
		    print 'found uniuq pair'
		    for item in other_terms:
			print 'getting split'
	    	        other_terms_temp.append(split_term(copy.deepcopy(item),list_ind[i1],list_ind[i2]))
		    other_terms.extend(other_terms_temp)
	final_terms.extend(other_terms)
    return final_terms
	
			
