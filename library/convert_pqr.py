#Usage : convert_pqr(list_terms), where list_terms should be a list of object of type terms.
#Purpose :This function produces all possible 'real' terms  from a term involving general indices 'pqr'. This means E^p_i will give
#E^j_i and E_a_i

#Algorithm : ------------------------------------------------------------------
#select one term from list_terms
#recursive convert function - if term doesnt contain pqr, append to final
#else : convert 1 pqr to i and a (producing 2 terms) and call convert to the rest

import print_terms
import copy
from next_op import next_op
def pqr_present(term):
    for coeff in term.coeff_list:
	for ind in coeff:
	    if len(ind)==2:
	        if term.isa(ind[0])==0 and term.isi(ind[0])==0:
		    return 1
	    else:
	        if term.isa(ind)==0 and term.isi(ind)==0:
		    return 1
    return 0
def ia_limit(term):
    a=0
    i=0
    p=0
    for key, value in term.dict_ind.items():

	if len(key)==1:
            if key>='a' and key<='h':
                a=a+1
            elif key>='p' and key<='t':
                p=p+1
            elif key>='i' and key<='n':
                i=i+1
	elif len(key)==2:
            if key[0]>='a' and key[0]<='h':
                a=a+1
            elif key[0]>='p' and key[0]<='t':
                p=p+1
            elif key[0]>='i' and key[0]<='n':
                i=i+1
    return [i,a,p]
def change_sum(term, oldi, newi):
    for ind in range(len(term.sum_list)):
	if term.sum_list[ind]==oldi:
	    term.sum_list[ind]=newi
    
    if term.st[0][-1].kind=='op':

	for ind in term.st[0][-1].upper:
	    if ind in term.sum_list:
		term.sum_list.remove(ind)
	for ind in term.st[0][-1].lower:
	    if ind in term.sum_list:
		term.sum_list.remove(ind)
    	

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
    else :
	print 'ERROR in change op in change+pqr. There is no op in the term. term is fully contracted yet has general indices'
def add_dict(term,coeff,newi):
    for i in range(len(term.coeff_list)):
	if term.coeff_list[i]==coeff:
	    term.dict_ind[newi]=term.map_org[i]
	    return term
def convert_single(term):

    final_terms=[]
    if pqr_present(term):
	#print 'in pqr_present'
	ia_list=ia_limit(term)
	flag=0
	for coeff in term.coeff_list:
	    for ind in range(len(coeff)):

	        #print  term.isa(coeff[ind]), term.isi(coeff[ind]) 
	        if term.isa(coeff[ind])==0 and term.isi(coeff[ind])==0 and flag==0:

    		    #print 'in convert single ,', term.sum_list
		    term=change_op(term,coeff[ind], next_op('i',ia_list,0))

		    #first change op before sum, to remove op ind in sum 
		    term=change_sum(term, coeff[ind], next_op('i',ia_list,0))
		    term=add_dict(term,coeff,next_op('i',ia_list,0))
	            coeff[ind]=next_op('i',ia_list,0)
		    final_terms.append(copy.deepcopy(term))
		    del term.dict_ind[coeff[ind]]
		    
		    term=change_sum(term, coeff[ind], next_op('a',ia_list,0))
		    term=change_op(term,coeff[ind], next_op('a',ia_list,0))
		    term=add_dict(term,coeff,next_op('a',ia_list,0))
		    coeff[ind]=next_op('a',ia_list,0)
		    final_terms.append(copy.deepcopy(term))
		    del term.dict_ind[coeff[ind]]
		    return final_terms
    else:
        final_terms.append(term)
    	return final_terms

    print 'ERROR :something wrong in pqr convert : other than pqr_present or not present happening!!!!!!!'
    return []
	
def convert(term):
    final_terms=[]
    final_terms=convert_single(term)
    #print 'first single', len(final_terms)

    while pqr_present(final_terms[0]):
	#print_terms.print_terms([final_terms[0]])
	inter_terms=[]
	for term in final_terms:
	    inter_terms.extend(convert_single(term))
	final_terms=inter_terms
        #print_terms.print_terms(final_terms)
    return final_terms
def convert_pqr(list_terms):
    final_terms=[]
    
    #print '---------------'
    for term in list_terms:
	final_terms.extend(convert(term))
    #print_terms.print_terms(final_terms)
    return final_terms

