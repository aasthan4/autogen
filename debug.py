from main_tools import product as math
from library import convert_pqr  
from  main_tools.commutator import comm
from library import pick
from library import print_terms
from library import rn_comm
from tests.debugcases import general_term 
#comm(['V2'],['T2'],1)
#list_terms=comm(comm(['V2'],['T2'],0),['T1'],1)
#list_terms=comm(['V2'],['T2'],1)
#print_terms.print_terms(list_terms)
#'''
term=general_term(['V2','T2','T1'])
list_terms=[term]

print_terms.print_terms(list_terms)
print 'general term creation done'
print 'printing done'
list_terms=convert_pqr.convert_pqr(list_terms)

#list_terms=print_terms.clean_list(list_terms)
#list_terms=pick.pick(list_terms, ['i'],['j'])

print '------'
print_terms.print_terms(list_terms)
print '------'
print 'conversion done'
#for item in list_terms:
#    print rn_comm.rank(item)

#list_terms=rn_comm.select_r(list_terms)

#print_terms.print_terms(list_terms)
#'''
