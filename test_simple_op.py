from tests import ccsd_amplitude as ccsd
from main_tools.commutator import comm
from main_tools.product import prod
from library import print_terms
from library import full_con

print 'case of [F,T1]'

list_terms=prod(['X2'],comm(comm(['V2'],['T2'],0),['T21'],0),1)
#list_terms=prod(['X2'],comm(comm(comm(['V2'],['T1'],0),['T11'],0),['D12'],0),1)
#list_terms=prod(['X2'],comm(comm(comm(['V2'],['T1'],0),['D11'],0),['T12'],0),1)
#list_terms=prod(['X2'],comm(comm(comm(['V2'],['T1'],0),['D11'],0),['D12'],0),1)
#list_terms=prod(['X2'],comm(comm(comm(['V2'],['D1'],0),['T11'],0),['T12'],0),1)
#list_terms=prod(['X2'],comm(comm(comm(['V2'],['D1'],0),['T11'],0),['D12'],0),1)
#list_terms=prod(['X2'],comm(comm(comm(['V2'],['D1'],0),['D11'],0),['T12'],0),1)
#list_terms=prod(['X2'],comm(comm(comm(['V2'],['D1'],0),['D11'],0),['D12'],0),1)
#The following function selects only the fully contracted terms from the above list_terms
#list_terms=full_con.full_terms(list_terms)
print_terms.print_terms(list_terms)
