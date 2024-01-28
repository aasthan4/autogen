from tests import ccsd_amplitude as ccsd
from main_tools.commutator import comm
from main_tools.driv3 import driver
from main_tools.product import prod
from library import print_terms
from library import full_con
from library import pick
from library import convert_pqr
from library import compare_envelope as ce
print 'case of '
list_terms=[]
list_terms1=[]
#
#Simple test for operators 1.0/6.0,['X1','V2','T1','T12','T13'])
list_terms=prod(['X1'],comm(comm(comm(['V2'],['T1'],0),['T11'],0),['T12'],0),1.0/6.0)
list_terms=full_con.full_terms(list_terms)
print_terms.print_terms(list_terms,'latex_output.txt')

#testing to pick suitable operators and then projecting to X
'''
list_terms=comm(comm(comm(['V2'],['T1'],0),['T11'],0),['T12'],1.0/6.0)

print_terms.print_terms(list_terms,'latex_output.txt')
list_terms1=pick.pick_test(list_terms,['a','b'],['i','j'])
print_terms.print_terms(list_terms1,'latex_output.txt')
list_terms=prod(['X1'],list_terms1,1.0)
list_terms=full_con.full_terms(list_terms)
print_terms.print_terms(list_terms,'latex_output.txt')
'''

'''
list_terms=prod(['X1'],comm(comm(comm(['V2'],['T1'],0),['T11'],0),['T12'],0),1.0/6.0)
list_terms=prod(['X1'],comm(comm(comm(['V2'],['T1'],0),['T12'],0),['D13'],0),-1.0/6.0)
list_terms=full_con.full_terms(list_terms)
print_terms.print_terms(list_terms,'ucc_X1VS1S1S1')
list_terms=prod(['X1'],comm(comm(comm(['V2'],['T1'],0),['D12'],0),['T13'],0),-1.0/6.0)
list_terms=full_con.full_terms(list_terms)
print_terms.print_terms(list_terms,'ucc_X1VS1S1S1')
list_terms=prod(['X1'],comm(comm(comm(['V2'],['T1'],0),['D12'],0),['D13'],0),1.0/6.0)
list_terms=full_con.full_terms(list_terms)
print_terms.print_terms(list_terms,'ucc_X1VS1S1S1')
list_terms=prod(['X1'],comm(comm(comm(['V2'],['D1'],0),['T12'],0),['T13'],0),-1.0/6.0)
list_terms=full_con.full_terms(list_terms)
print_terms.print_terms(list_terms,'ucc_X1VS1S1S1')
list_terms=prod(['X1'],comm(comm(comm(['V2'],['D1'],0),['T12'],0),['D13'],0),1.0/6.0)
list_terms=full_con.full_terms(list_terms)
print_terms.print_terms(list_terms,'ucc_X1VS1S1S1')
list_terms=prod(['X1'],comm(comm(comm(['V2'],['D1'],0),['D12'],0),['T13'],0),1.0/6.0)
list_terms=full_con.full_terms(list_terms)
print_terms.print_terms(list_terms,'ucc_X1VS1S1S1')
list_terms=prod(['X1'],comm(comm(comm(['V2'],['D1'],0),['D12'],0),['D13'],0),-1.0/6.0)
list_terms=full_con.full_terms(list_terms)
print_terms.print_terms(list_terms,'ucc_X1VS1S1S1')

#The following function selects only the fully contracted terms from the above list_terms
'''
