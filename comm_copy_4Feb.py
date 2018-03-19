#Problem 1 : make op returns a list of Large OPerators. 
#in order to put it on a same footing as make_cont output, aop=aop[0]
import copy
import pkg.library.print_terms as pt
import pkg.library.make_op as make_op
import pkg.library.change_terms as ct 
import pkg.library.class_term as class_terms
import pkg.library as lib
import multi_cont
'''
class list_op_term:
    def __init__(self, sign,list_op):
        self.sign=sign
        self.list=list_op
    def print1(self):
         print self.sign,self.list
'''
#comm should accept a list of terms/Alphabet operator and list of terms/Alphabet operator.
#1-> commutator on 2-> commutator off so only 1 term
def comm(a,b):
    #intelligently check input
    if a[0].isalnum():
	#build operator
	a,a_dict_ind=make_op.make_op(a)
	a=a[0] #refer to the header
	a.map_org=[a]
    # else a is a list of terms contract directly.
    #repeat for b
    if b[0].isalnum():
	name2=b
	b,b_dict_ind=make_op.make_op(b)
	b=b[0]
	b.map_org=[b]
	#print 'map of b', b.name, b.map_org
    #so aop is a list of operators not just an operator how to deal with it on the same footing as the result of a cont
    #contract a,b and store in list_terms
    st1,co1=multi_cont.multi_cont(a.st,b.st,a.co,b.co)
    #contract b,a and store in list lerms
    st2,co2=multi_cont.multi_cont(b.st,a.st,b.co,a.co)
    #testing printing
    lib.print_op.print_op(st1,co1)

    #add all the dictionaries
    dict_add=dict(a_dict_ind.items()+b_dict_ind.items())
    #if large operators add a and b in a list
    #if string of operators use amaporg and bmaporg
    
    #make terms of st and co and list of terms
    list_terms=ct.change_terms1(st1,co1,dict_add, a.map_org+b.map_org)#Problem : how to make lou?
    list_terms.extend(ct.change_terms1(st2,co2,dict_add, b.map_org+a.map_org))
    for item in list_terms:
	item.compress()
	item.build_map_org()
	#item.cond_cont(dict_add)
    	item.print_term()
	#till now generated till generating all expresions for large opeerators. 
	#now selecting them, then extendint the code for a random st of operators
	#then add an extra multiplier on the left
    #think about reducing list terms by eliminating same terms.




    #compare terms based on 5 levels of check all in cpre.compare()

    for i in range(len(list_terms)):
        for  j in range(i+1,len(list_terms)):
            if list_terms[i].fac!=0 and list_terms[j].fac!=0:
                #print "comparing inside drive -------:", i,j,list_terms[i].coeff_list, list_terms[j].coeff_list
                flo= cpre.compare(list_terms[i],list_terms[j])
                if flo!=0:
                    #print 'result in the comparision',i,j,flo
                    #print 'this should be 0 always = ',list_terms[i].fac+list_terms[j].fac*flo
                    list_terms[i].fac=list_terms[i].fac+list_terms[j].fac * flo
                    list_terms[j].fac=0.0

    #muliply with the prefactor of the expression from the Housdoff Expression
    for item in list_terms:
        if item.fac!=0.0:
            item.fac=item.fac*fc

    #print list_terms[i].fac, list_terms[j].fac


    #for term in list_terms:
        #if term.fac!=0:
            #print term.fac, term.sum_list, term.coeff_list

    #print terms properly
    pt.print_terms(list_terms) 
    return list_terms 

comm(['F1'],['T1'])
