#problem 1: the permutation is to be taken care of
#problem 2 : always use term.cond_cont() for after change_term functions to create term objects (teh condition is that there should be atleast one contraction with H)
#problem 3: map org should be added inside change term while creating term objects.
#problem 4 : while printing just F1 and T1, it skips the first large operator which in the present case is X1.
#correction 5: dont need dict in change_term in library please delete
#note 6 : term.mapping() stores names of Large op in map_org and build_map_org stores operators
#immediate task : X1 T1 etc are not in one go so a i etc are threr twice. change that just pass dict
from . import multi_cont
import library as lib
import library.change_terms as ct
import library.print_terms as pt
import library.compare as cpre

def driver(fc,list_char_op):
#def driver(fc):
    #build operators
    #list_char_op=['D2','V2','Y2']
    dict_ind={}
    lou, dict_ind=lib.make_op.make_op(list_char_op, dict_ind)
    #Do contractions
    a=lou[0].st
    b=lou[0].co
    #lib.print_op.print_op(lou[0].st,lou[0].co)
    for i in range(1,len(lou)):
        a,b=multi_cont.multi_cont(a, lou[i].st, b, lou[i].co)
        #lib.print_op.print_op(lou[i].st,lou[i].co)

        #lib.print_op.print_op(a,b)
        #print '------'
        #a,b=multi_cont.multi_cont(a,lou[2].st, b, lou[2].co)
        #a,b=multi_cont.multi_cont(a,lou[3].st, b, lou[3].co)

    #fully contracted only
    a,b=lib.full_con.full_con(a,b)
    #lib.print_op.print_op(a,b)

    #Changing t,c to object terms.(bug 19Feb2020 comes into already int,c) 
    list_terms=ct.change_terms1(a,b,fc,dict_ind, lou)

    #compress terms eliminating deltas
    for term in list_terms:
        term.compress()
        #print dict_ind
        #condition for atleast 1 contraction with H
        term.cond_cont(dict_ind)
        term.build_map_org()
        term.print_term()
    print(( 'list terms full con length', len(list_terms)))
    #---
    #for term in list_terms:
        #term.print_term()
    print( '-------final below----')
    '''
    #integral symmetry
    for i in range(len(list_terms)):
        for j in range(i+1, len(list_terms)):


            if list_terms[i].fac!=0 and list_terms[j].fac!=0:
                flo= list_terms[i].compare(list_terms[j])
                if flo!=0:
                    #print i,j,flo
                    list_terms[i].fac=list_terms[i].fac+list_terms[j].fac * flo
                    list_terms[j].fac=0.0
    #for item in list_terms:
        #if item.fac!=0:
            #print 'yay'
    #dummy_check
    for i in range(len(list_terms)):
        for j in range(i+1,len(list_terms)):
            if list_terms[i].fac!=0 and list_terms[j].fac!=0:
                #print list_terms[i].fac, list_terms[j].fac
                list_terms[i].dummy_check(list_terms[j])

    '''
    #compare terms based on 5 levels of check all in cpre.compare()
    for i in range(len(list_terms)):
        for  j in range(i+1,len(list_terms)):
            if list_terms[i].fac!=0 and list_terms[j].fac!=0:
                #print "comparing inside drive -------:", i,j,list_terms[i].coeff_list, list_terms[j].coeff_list
                flo= cpre.compare(list_terms[i],list_terms[j])
                if flo!=0:
                    #print 'in result in the comparision',i,j,flo
                    #print 'this should be 0 always = ',list_terms[i].fac+list_terms[j].fac*flo
                    list_terms[i].fac=list_terms[i].fac+list_terms[j].fac * flo
                    list_terms[j].fac=0.0
                #print 'out result in the comparision',i,j,list_terms[i].coeff_list,list_terms[j].coeff_list,flo

    #muliply with the prefactor of the expression from the Housdoff Expression(No need to do this now)
    #for item in list_terms:
    #    if item.fac!=0.0:
    #        item.fac=item.fac*fc

    #print list_terms[i].fac, list_terms[j].fac


    #for term in list_terms:
        #if term.fac!=0:
            #print term.fac, term.sum_list, term.coeff_list

    #print terms properly
    pt.print_terms(list_terms,'latex_output.txt')
#driver(1.0)
