from tests import ccsd_amplitude as ccsd

from main_tools.commutator import comm
from main_tools import product as math2
from library import full_con
from library import convert_pqr
from library import pick
from library import compare_envelope as ce
from library import print_terms as pt
import library
from library.rn_comm import select_r
from library.symmetric import symm
#ccsd.amplitude()

list_terms1=[]
list_terms2=[]
list_terms3=[]
list_terms4=[]
list_terms5=[]
list_terms6=[]
list_terms7=[]
list_terms8=[]
list_terms=[]


list_terms1.extend(comm(comm(['V2'],['D1'],0),['D11'],1))

#list_terms1.extend(comm(['V2'],['T2'],1))
#list_terms.extend(select_r(comm(['V2'],['T1'],1)))

#list_terms1.extend(comm(list_terms,['T21'],1))

list_terms=library.convert_pqr.convert_pqr(list_terms1)

library.print_terms.print_terms(list_terms)

list_terms1=pick.pick(list_terms,['i'],['j'])
list_terms2=pick.pick(list_terms,['a'],['b'])
list_terms3=pick.pick(list_terms,['i','j'],['k','l'])
list_terms4=pick.pick(list_terms,['a','b'],['c','d'])
list_terms5=pick.pick(list_terms,['i','a'],['b','j'])


'''
list_terms2.extend(math1.comm(math1.comm(['V2'],['T2'],0),['D21'],-1))
list_terms3.extend(math1.comm(math1.comm(['V2'],['D2'],0),['T21'],-1))
list_terms4.extend(math1.comm(math1.comm(['V2'],['D2'],0),['D21'],1))
'''
'''
list_terms5.extend(math1.comm(math1.comm(['V2'],['T1'],0),['T2'],1))
list_terms6.extend(math1.comm(math1.comm(['V2'],['T1'],0),['D2'],-1))
list_terms7.extend(math1.comm(math1.comm(['V2'],['D1'],0),['T2'],-1))
list_terms8.extend(math1.comm(math1.comm(['V2'],['D1'],0),['D2'],1))
'''
list_terms=list_terms1+list_terms2+list_terms3+list_terms4+list_terms5#+list_terms6+list_terms7+list_terms8



list_terms1=ce.compare_envelope(list_terms1,1,1)
list_terms2=ce.compare_envelope(list_terms2,1,1)
list_terms3=ce.compare_envelope(list_terms3,1,1)
list_terms4=ce.compare_envelope(list_terms4,1,1)
list_terms5=ce.compare_envelope(list_terms5,1,1)

list_terms1=pt.clean_list(list_terms1)
list_terms2=pt.clean_list(list_terms2)
list_terms3=pt.clean_list(list_terms3)
list_terms4=pt.clean_list(list_terms4)
list_terms5=pt.clean_list(list_terms5)

list_terms1=symm(list_terms1)
list_terms2=symm(list_terms2)
list_terms3=symm(list_terms3)
list_terms4=symm(list_terms4)
list_terms5=symm(list_terms5)

library.print_terms.print_terms(list_terms1)
library.print_terms.print_terms(list_terms2)
library.print_terms.print_terms(list_terms3)
library.print_terms.print_terms(list_terms4)
library.print_terms.print_terms(list_terms5)
