def clean_list(list_terms):
    final_terms=[]
    for term in list_terms:

        #if term.fac!=0.0 and abs(term.fac)>0.0000001:
        if term.fac!=0.0:
            #print term.fac
            final_terms.append(term)
    #print 'length of final terms',len(final_terms)
    return final_terms
def print_terms(list_terms,filename):
    pfile=open(filename,'a')
    for term in list_terms:
        if term.fac!=0.0:
            term.print_term()
            term.print_latex(pfile)
    pfile.write("------------\\\\ \n")
