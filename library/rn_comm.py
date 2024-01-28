##These sett of functions chose the R or N part of a commutator
#NOTE : This is based on a Singles and Doubles Theory so [ ] of more than rank possible of 2 automattically become R
#only works once worked with convert_pqr to get rid of general indices
def rank(term):
    rnk=0.0
    if term.st[0][-1].kind=='op':
        #a and i in upper and lower +1/2
        #a and i in lower and upper is -1/2
        up=term.st[0][-1].upper
        lo=term.st[0][-1].lower

        for ind in up:
            if term.isi(ind)==1:
                rnk=rnk-0.5
            elif term.isa(ind)==1:
                rnk=rnk+0.5
            else:
                print('problem in functiton rank in library/rn_comm')
                #sys.end()
        for ind in lo:
            if term.isi(ind)==1:
                rnk=rnk+0.5
            elif term.isa(ind)==1:
                rnk=rnk-0.5
            else:
                print('problem in functiton rank in library/rn_comm')
                #.end()
        return rnk
    else :
        #rank of a fully contracted term is -100 
        return -100


def select_n(list_terms):
    final_terms=[]
    for term in list_terms:
        #not fully contracted
        if rank(term)!=-100 :
            if len(term.st[0][-1].upper)==2:
                if rank(term)==2 or rank(term)==-2:
                    final_terms.append(term)
            if len(term.st[0][-1].upper)==1:
                if rank(term)==1 or rank(term)==-1:
                    final_terms.append(term)
    return final_terms
def select_r(list_terms):
    final_terms=[]
    for term in list_terms:
        #not fully contracted
        if rank(term)!=-100 :
            if len(term.st[0][-1].upper)==2:
                if rank(term)!=2 and rank(term)!=-2:
                    final_terms.append(term)
            if len(term.st[0][-1].upper)==1:
                if rank(term)!=1 and rank(term)!=-1:
                    final_terms.append(term)
        else:
            final_terms.append(term)
    return final_terms
