def clean_list(list_terms):
    final_terms=[]
    for term in list_terms:
	if term.fac!=0.0:
	    final_terms.append(term)
    return final_terms
def print_terms(list_terms):
    pfile=open('latex_output.txt','a')
    for term in list_terms:
        #if term.fac!=0.0:
        term.print_term()
        #term.print_latex(pfile)
    pfile.write("------------\\\\ \n")
