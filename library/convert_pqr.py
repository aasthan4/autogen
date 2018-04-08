#Usage : convert_pqr(list_terms), where list_terms should be a list of object of type terms.
#Purpose :This function produces all possible 'real' terms  from a term involving general indices 'pqr'. This means E^p_i will give
#E^j_i and E_a_i

#Algorithm : ------------------------------------------------------------------
#select one term from list_terms
#recursive convert function - if term doesnt contain pqr, append to final
#else : convert 1 pqr to i and a (producing 2 terms) and call convert to the rest

import print_terms
import copy
def pqr_present(term):
    for coeff in term.coeff_list:
	for ind in coeff:
	    if term.isa(ind)==0 and term.isi(ind)==0:
		return 1
    return 0
def ia_limit(term):
    a=0
    i=0
    p=0
    for key, value in term.dict_ind.items():

        if key>='a' and key<='h':
            a=a+1
        elif key>='p' and key<='t':
            p=p+1
        elif key>='i' and key<='n':
            i=i+1
    return [i,a,p]
def change_sum(term, oldi, newi):
    for ind in range(len(term.sum_list)):
	if term.sum_list[ind]==oldi:
	    term.sum_list[ind]=newi
	    return term	
def change_op(term, oldi, newi):
    if term.st[0][-1].kind=='op':
        for ind in range(len(term.st[0][-1].upper)):
            if term.st[0][-1].upper[ind]==oldi:
	        term.st[0][-1].upper[ind]=newi
	        return term
        for ind in range(len(term.st[0][-1].lower)):
            if term.st[0][-1].lower[ind]==oldi:
	        term.st[0][-1].lower[ind]=newi
	        return term
def add_dict(term,coeff,newi):
    for i in range(len(term.coeff_list)):
	if term.coeff_list[i]==coeff:
	    term.dict_ind[newi]=term.map_org[i]
	    return term
def convert(term):
    final_terms=[]
    if pqr_present(term):
        ia_list=ia_limit(term)

        flag=0
	for coeff in term.coeff_list:
	    for ind in range(len(coeff)):
	        if term.isa(coeff[ind])==0 and term.isi(coeff[ind])==0 and flag==0:
		    term=change_sum(term, coeff[ind], chr(ord('i')+ia_list[0]))
		    term=change_op(term,coeff[ind], chr(ord('i')+ia_list[0]))
		    term=add_dict(term,coeff,chr(ord('i')+ia_list[0]))
	            coeff[ind]=chr(ord('i')+ia_list[0])
		    final_terms.extend(convert(copy.deepcopy(term)))
		    del term.dict_ind[coeff[ind]]
		    
		    term=change_sum(term, coeff[ind], chr(ord('a')+ia_list[1]))
		    term=change_op(term,coeff[ind], chr(ord('a')+ia_list[1]))
		    term=add_dict(term,coeff,chr(ord('a')+ia_list[1]))
		    coeff[ind]=chr(ord('a')+ia_list[1])
		    final_terms.extend(convert(copy.deepcopy(term)))
		    del term.dict_ind[coeff[ind]]
		    flag=1
    else:
        final_terms.append(term)
    return final_terms
def convert_pqr(list_terms):
    final_terms=[]
    print '---------------'
    for term in list_terms:
	final_terms.extend(convert(term))
    #print_terms.print_terms(final_terms)
    return final_terms

