#accompanied always with term.cond_cont in order to generate map_org
#dont need the dict correct later
import class_term
import print_op
import copy
def change_terms1(a, b, fac,dict_ind, list_op_used):

    sum_ind=[]
    coeff=[]
    list_terms=[]

    for op in list_op_used:
        fac=op.fac*fac
        sum_ind.extend(op.sum_ind)
        coeff.append(op.coeff)
	
    for (t,c)  in zip(a,b):
	t=[t]#as t is a list of terms and each term has operators like delta and op
	c=[c]
	#to make coeff list of the operator so that it can be compared in the comaprer funciton
	'''
	if t[0][-1].kind='op':
	    make_coeff=[]
	    for item in t[0][-1].upper:
		make_coeff.append(item)
	    for item in t[0][-1].lower:
		make_coeff.append(item)
	coeff_list.append(make_coeff)
	'''
	flag=0
	for item in t[0]:
	    if item.kind=='op':
	        temp=[]
	        flag=1
	        temp.extend(item.upper)
	        temp.extend(item.lower)
	if flag==1:
	    coeff.append(temp)
	print 'in change terms',coeff
        x=class_term.term(copy.copy(fac*c[0][0]), copy.copy(sum_ind), copy.copy(coeff), list_op_used,t, c)
	x.dict_ind=dict_ind
	if flag==1:
	    coeff.pop()
	#print c
	#print_op.print_op(t,c)
        #print c,fac, sum_ind, coeff
        list_terms.append(x)
	
    return list_terms

