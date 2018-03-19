#problem 1: the permutation is to be taken care of 
import multi_cont
import pkg.library as lib
import pkg.library.change_terms as ct
import pkg.library.print_terms as pt

#def driver(list_char_op):
def driver():
    #build operators
    list_char_op=['X1','V2','T2']
    lou, dict_ind=lib.make_op.make_op(list_char_op)  
    #Do contractions
    a=lou[0].st
    b=lou[0].co
    for i in range(1,len(lou)):
        a,b=multi_cont.multi_cont(a, lou[i].st, b, lou[i].co)
    

        #lib.print_op.print_op(a,b)
        #print '------'
        #a,b=multi_cont.multi_cont(a,lou[2].st, b, lou[2].co)
        #a,b=multi_cont.multi_cont(a,lou[3].st, b, lou[3].co)

    #fully contracted
    a,b=lib.full_con.full_con(a,b)
    lib.print_op.print_op(a,b)


    #change to terms
    list_terms=ct.change_terms1(a,b,dict_ind, lou)

    #compress terms eliminating deltas
    for term in list_terms:
        term.compress()
        #print dict_ind
        #condition for atleast 1 contraction with H 
        term.cond_cont(dict_ind)
        
    #---
    #for term in list_terms:
    #    term.print_term()
    #print '-------final below----'
    
    #integral symmetry
    pos2body=[]
    for item in lou:
        if item.name[1]=='2' and item.name[0]!='X':
            pos2body=lou.index(item)
    for pos in pos2body:
        for i in range(len(list_terms)):
            for j in range(i+1, len(list_terms)):
                if list_terms[i].fac!=0 and list_terms[j].fac!=0:
                    flo= list_terms[i].compare(list_terms[j], pos)
                    #print Vpos, flo
                    if flo!=0:
                        list_terms[i].fac=list_terms[i].fac+list_terms[j].fac * flo
                        list_terms[j].fac=0.0
                        #print 'parent term'
                        #list_terms[i].print_term()
                        #print 'baby term'
                        #list_terms[j].print_term()
    #for item in list_terms:
        #if item.fac!=0:
            #print 'yay'
    #dummy_check
    for i in range(len(list_terms)):
        for j in range(i+1,len(list_terms)):
            if list_terms[i].fac!=0 and list_terms[j].fac!=0:
                #print list_terms[i].fac, list_terms[j].fac
                list_terms[i].dummy_check(list_terms[j])



    #print list_terms[i].fac, list_terms[j].fac


    #for term in list_terms:
    #    print term.fac, term.sum_list,term.coeff_list
    
    #print terms properly
    pt.print_terms(list_terms)
driver()
