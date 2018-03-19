import multi_cont
import pkg.library as lib
import pkg.library.change_terms as ct
import pkg.library.print_terms as pt
def driver():
    list_char_op=['X2','V', 'T1']
    lou, dict_ind=lib.make_op.make_op(list_char_op)  

    
    a,b=multi_cont.multi_cont(lou[0].st, lou[1].st, lou[0].co, lou[1].co)
    a,b=multi_cont.multi_cont(a,lou[2].st, b, lou[2].co)


    #List of operators multiplied :
    #list_op_used=[X2, F, T1, T1]

    #fully contracted
    a,b=lib.full_con.full_con(a,b)
    lib.print_op.print_op(a,b)

    #change to terms
    list_terms=ct.change_terms1(a,b,dict_ind, lou)
    for term in list_terms:
        term.compress()
    
    for term in list_terms:
        print '-',term.fac, term.coeff_list

    
    #integral symmetry
    Vpos=-1
    for item in lou:
        if item.name=='V':
            Vpos=lou.index(item)

    for i in range(len(list_terms)):
        for j in range(i+1, len(list_terms)):
            flo= list_terms[i].compare(list_terms[j], Vpos)
            if flo!=0:
                list_terms[i].fac=list_terms[i].fac+list_terms[j].fac * flo
                list_terms[j].fac=0.0
            
    #for term in list_terms:
    #    print term.fac, term.sum_list,term.coeff_list
    
    #print terms properly
    pt.print_terms(list_terms)
driver()
