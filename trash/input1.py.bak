from tests import ccsd_amplitude as ccsd
from main_tools.commutator import comm
from main_tools.driv3 import driver
from main_tools.product import prod
from library import print_terms
from library import full_con
from library import pick
from library import convert_pqr
from library import compare_overall2 as ce
from library import compare_test as ctest
from library import h_third as ht
print 'case of '
list_terms=[]
list_terms1=[]

'''
test0
list_terms=prod(['X1'],comm(comm(['V2'],['T11'],0.0),['T12'],0),0.5)
list_terms.extend(prod(['X1'],comm(comm(['V2'],['D11'],0.0),['T12'],0),-0.5))
list_terms.extend(prod(['X1'],comm(comm(['V2'],['T11'],0.0),['D12'],0),-0.5))
list_terms.extend(prod(['X1'],comm(comm(['V2'],['D11'],0.0),['D12'],0),0.5))
'''
'''
#test1
list_terms=prod(['X2'],comm(comm(['V2'],['T11'],0.0),['T12'],0),0.5)
list_terms.extend(prod(['X2'],comm(comm(['V2'],['D11'],0.0),['T12'],0),-0.5))
list_terms.extend(prod(['X2'],comm(comm(['V2'],['T11'],0.0),['D12'],0),-0.5))
list_terms.extend(prod(['X2'],comm(comm(['V2'],['D11'],0.0),['D12'],0),0.5))
'''
'''
#test2
list_terms1=prod(['X2'],comm(comm(comm(['V2'],['T11'],0),['D12'],0),['T13'],0),-1.0)
list_terms1=ht.select_hthird(list_terms1)
list_terms2=prod(['X2'],comm(comm(comm(['V2'],['D11'],0),['T12'],0),['T13'],0),-1.0)
list_terms2=ht.select_hthird(list_terms2)
list_terms3=prod(['X2'],comm(comm(comm(['V2'],['T11'],0),['T12'],0),['D13'],0),-1.0)
list_terms3=ht.select_hthird(list_terms3)
list_terms=list_terms1+list_terms2+list_terms3
#list_terms=list_terms2
print 'finished'
'''
#test3

list_terms1=prod(['X2'],comm(comm(comm(['V2'],['D21'],0),['T12'],0),['T23'],0),-1.0)
list_terms1=ht.select_hthird(list_terms1)
list_terms2=prod(['X2'],comm(comm(comm(['V2'],['T11'],0),['D22'],0),['T23'],0),-1.0)
list_terms2=ht.select_hthird(list_terms2)
list_terms3=prod(['X2'],comm(comm(comm(['V2'],['D21'],0),['T22'],0),['T13'],0),-1.0)
list_terms3=ht.select_hthird(list_terms3)
list_terms4=prod(['X2'],comm(comm(comm(['V2'],['T21'],0),['D22'],0),['T13'],0),-1.0)
list_terms4=ht.select_hthird(list_terms4)
list_terms5=prod(['X2'],comm(comm(comm(['V2'],['T21'],0),['T12'],0),['D23'],0),-1.0)
list_terms5=ht.select_hthird(list_terms5)
list_terms6=prod(['X2'],comm(comm(comm(['V2'],['T11'],0),['T22'],0),['D23'],0),-1.0)
list_terms6=ht.select_hthird(list_terms6)
list_terms=list_terms1+list_terms2+list_terms3+list_terms4+list_terms5+list_terms6
list_terms=full_con.full_terms(list_terms)



#list_terms.extend(prod(['X2'],comm(comm(comm(['V2'],['T21'],0),['D12'],0),['T23'],0),-1.0/6.0))
#list_terms=full_con.full_terms(list_terms)
'''
list_terms.extend(prod(['X2'],comm(comm(comm(['V2'],['D21'],0),['D22'],0),['T23'],0),1.0/6.0))
list_terms.extend(prod(['X2'],comm(comm(comm(['V2'],['T21'],0),['D22'],0),['D23'],0),1.0/6.0))
list_terms.extend(prod(['X2'],comm(comm(comm(['V2'],['D21'],0),['T22'],0),['D23'],0),1.0/6.0))
list_terms=full_con.full_terms(list_terms)
'''
#list_terms.extend(prod(['X1'],comm(comm(['V2'],['T11'],0),['T12'],0),1.0))



#list_terms=prod(['X2'],comm(['V2'],['T21'],0),1.0)
#list_terms.extend(prod(['X2'],comm(['V2'],['T21'],0),1.0))
#list_terms=prod(['X2'],comm(comm(['V2'],['T21'],0),['T22'],0),1.0)
#list_terms.extend(prod(['X2'],comm(comm(['V2'],['T21'],0),['T22'],0),1.0))
list_terms=full_con.full_terms(list_terms)

print 'inside main compare'
#print_terms.print_terms(list_terms,'latex_output.txt')
list_terms=ce.compare_envelope(list_terms,1.0,1)



print_terms.print_terms(list_terms,'factorcheck.txt')
#print_terms.print_terms(list_terms,'ucc_X1VD2T2T2.txt')

#driver(1.0/6.0,['X1','V2','T1','T12','T13'])

#list_terms=prod(['X1'],comm(comm(comm(['V2'],['T1'],0),['T11'],0),['T12'],0),1.0/6.0)

#list_terms=full_con.full_terms(list_terms)
#print_terms.print_terms(list_terms,'latex_output.txt')

