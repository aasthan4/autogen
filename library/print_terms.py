def print_terms(list_terms):
    pfile=open('latex_output.txt','a')
    for term in list_terms:
        if term.fac!=0.0:
            term.print_term()
            term.print_latex(pfile)
            #print term.fac, term.sum_list, term.coeff_list, term.large_op_list
