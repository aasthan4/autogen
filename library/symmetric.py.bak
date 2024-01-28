import copy
#make unique function
def unique(i1,i2,term):
    if term.dict_ind[i1]!=term.dict_ind[i2]:
        if i1 in term.st[0][-1].upper and i2 in term.st[0][-1].upper and term.type(i1)==term.type(i2):
            return 1
        elif i1 in term.st[0][-1].lower and i2 in term.st[0][-1].lower and term.type(i1)==term.type(i2):
            return 1
    return 0
#make split_terms
def split_term(term,i1,i2):
   term.fac=term.fac*-1
   for coeff in term.coeff_list:
        for ind in range(len(coeff)):
            if coeff[ind]==i1:
                 coeff[ind]=i2
            elif coeff[ind]==i2:
                coeff[ind]=i1
   return copy.deepcopy(term)
#Algo : Make a list of all undummy indices
#----find the unique pairs in them if found split into two 
def symm(list_terms):
    final_terms=[]
    for term in list_terms:
        #this task has to be done on each term on other term as well
        other_terms=[]
        list_ind=[]
        other_terms_temp=[]
        other_terms.append(term)
        #make a list of ind for finding unie pairs
        print(term.st[0][-1].upper, term.st[0][-1].lower)
        for coeff in term.coeff_list:
            for ind in coeff:
                if ind not in term.sum_list:
                    list_ind.append(ind)
        print(list_ind)
        #find unique pairs and split terms into two or multiple of twos
        for i1 in list_ind:
            for i2 in list_ind:
                if unique(i1,i2, term) and i1!=i2:
                    print('found uniuq pair', i1,i2)
                    for item in other_terms:
                        item.fac=item.fac/2.0
                        print('getting split')
                        other_terms_temp.append(split_term(copy.deepcopy(item),i1,i2))
                    other_terms.extend(other_terms_temp)
                    other_terms_temp=[]
                    #delete inds from list_terms which are counted
                    list_ind.remove(i1)
                    list_ind.remove(i2)
        final_terms.extend(other_terms)
    return final_terms
        
                        
