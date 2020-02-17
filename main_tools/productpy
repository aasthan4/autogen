#in order to put it on a same footing as make_cont output, aop=aop[0]
#Incomplete 2 : when both terms of a commutator are computed, comparing and adding and subtracting should take place
# to get rid of the first term.
#Problem incomplete : in compare level 3 : in case of T1T2VD1D2, both are not permuted together. they are separate.
#Possible bug : in compare function line 58, the range of coeff starts from 0, 0 can be an X type operator
import copy
import library.print_terms as pt
import library.make_op as make_op
import library.change_terms as ct
import library.class_term as class_terms
import library as lib
import library. compare as cpre
import multi_cont
import library.compare_envelope as cpre_env
from library import full_con
removed=0
'''
class list_op_term:
    def __init__(self, sign,list_op):
        self.sign=sign
        self.list=list_op
    def print1(self):
         print self.sign,self.list
'''
#comm should accept a list of terms/Alphabet operator and list of terms/Alphabet operator.
#1-> commutator on 2-> commutator off so only 1 term on-> whether commutator is on or it is just a product
# last-> if its the outside last commutator or not (for taking the fully contracted terms)
def prod(a,b,last):
    on=0
    #????assume prefactor of the term to be 1
    fc=1.0

    #develop dict_ind
    if type(a[0])==str and type(b[0])==str:
	dict_add={}
    elif type(a[0]) ==str or type(b[0])==str:

	if type(a[0])==str:
	    dict_add=b[0].dict_ind
	elif type(b[0])==str:
	    dict_add=a[0].dict_ind
    else :
        dict_add=dict(a[0].dict_ind.items()+b[0].dict_ind.items())
    #intelligently check input
    if type(a[0])==str:
	#build operator
	a,a_dict_add=make_op.make_op(a, dict_add)
	#a=a[0] #refer to the header
	a[0].map_org=a
    # else a is a list of terms contract directly.
    if type(b[0])==str:
	name2=b
	b,b_dict_add=make_op.make_op(b,dict_add)
	#b=b[0]
	b[0].map_org=b
    #????so aop is a list of operators not just an operator how to deal with it on the same footing as the result of a cont
    #contract a,b and store in list_terms
    st2=[]
    st1=[]
    co2=[]
    co1=[]
    for t1 in a:
	for t2 in b:
	
	
    	    stt,cot=multi_cont.multi_cont(t1.st,t2.st,t1.co,t2.co)
	    #COMMUTATOR CONDITION : removing element where length of input operator strings =
	    #length of output operator string

	    for (term,termco) in zip(stt,cot):
		#lib.print_op.print_op(term,termco)
		


		present_op=0
		present_op1=0
		present_op2=0
		removed=0
		for op in term:
		    for op1 in t1.st[0]:
			for op2 in t2.st[0]:
		    	    if op.kind=='op' and op1.kind=='op' and op2.kind=='op' and len(op.upper)==(len(op1.upper)+len(op2.upper)):
		                #print 'there is a problem here', op.kind, len(op.upper),len(op1.upper),len(op2.upper)
				removed=1
				stt.remove(term)
				cot.remove(termco)
			    if op2.kind=='op':
				present_op2=1
			if op1.kind=='op':
		            present_op1=1
		    if op.kind=='op':
			present_op2=1
		if present_op1==0 or present_op2==0:
		    if removed==0:
		        #print 'here in fully contracted'
		        stt.remove(term)
    		        cot.remove(termco)
	    #print 'length of output string', len(stt)
	    st1.extend(stt)
	    co1.extend(cot)
    if last!=0:
	fc=last
    #make terms of st and co and list of terms
    list_terms=ct.change_terms1(st1,co1,fc,dict_add, a[0].map_org+b[0].map_org)#Problem : how to make lou?
    if on==1:
	terms_tmp=ct.change_terms1(st2,co2,fc,dict_add, b[0].map_org+a[0].map_org)
        for item in terms_tmp:
	    item.fac=item.fac*-1
	list_terms.extend(terms_tmp)
    for item in list_terms:
	item.compress()
	item.build_map_org()
	
    list_terms=full_con.full_terms(list_terms)
    cpre_env.compare_envelope(list_terms, fc, last)    
    return list_terms




'''
comm(['X2'], comm(['V2'],['D1'],1,0),0,1)

comm(['X2'], comm(['V2'],['T2'],1,0),0,1)
comm(['X2'], comm(['V2'],['D2'],1,0),0,1)
'''
