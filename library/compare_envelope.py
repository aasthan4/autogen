import compare as cpre
import print_terms as pt

def compare_envelope(list_terms, fc,last):
    #compare terms based on 5 levels of check all in cpre.compare()
    #for i in range(1):
	#for j in range(1,2):
    for i in range(len(list_terms)):
        for  j in range(i+1,len(list_terms)):
            if list_terms[i].fac!=0 and list_terms[j].fac!=0:
                #print "comparing inside drive -------:", i,j,list_terms[i].coeff_list, list_terms[j].coeff_list
                flo= cpre.compare(list_terms[i],list_terms[j])
                #print flo
                if flo!=0:

                    #print 'result in the comparision',i,j,flo
                    #print 'this should be 0 always = ',list_terms[i].fac+list_terms[j].fac*flo
                    list_terms[i].fac=list_terms[i].fac+list_terms[j].fac * flo
                    list_terms[j].fac=0.0
                #print 'result in the comparision',i,j,flo

    #muliply with the prefactor of the expression from the Housdoff Expression
    #for item in list_terms:
        #if item.fac!=0.0:
            #item.fac=item.fac*fc
    
    #print terms properly
    if last!=0:
	    
        #pt.print_terms(list_terms)
        #delete operator coefficient in self.coeff_list
        for term in list_terms:
	    if len(term.coeff_list)==len(term.map_org)+1:
	        #print 'deleting operator coeff'
	        term.coeff_list.pop()
	    elif len(term.coeff_list)>len(term.map_org):
	        print ' in compare envolope terminal error'
	        sys.exit(0)
    ##list_terms=pt.clean_list(list_terms)
    return list_terms
