#from tests import ccsd_amplitude as ccsd
from main_tools.commutator import comm
from library import print_terms
from library import full_con

#the input of the commutator function is as follows :
#if you want a commutator [V,T2]-> comm['op1'],['op2'],prefactor)
#NOTE : prefactor should be 0 in case this is not the last of the nested prefactor (clearer in the next eexample)

print('case of [V,T1]')
list_terms=prod(['V2'],['T1'],1)
print_terms.print_terms(VT1example)

print('case of [V,T2]')
list_terms=comm(['V2'],['T2'],1)
#The following function selects only the fully contracted terms from the above list_terms
list_terms=full_con.full_terms(list_terms)
print_terms.print_terms(list_terms)

#Case of a nested commutator :
#Note that the name of the operators of the same type are different 
#Like T1,T11,T12,T13 etc
print('case of [[V,T1],T1]')
list_terms=comm(comm(['V2'],['T1'],0),['T11'],1.0)
list_terms=full_con.full_terms(list_terms)
print_terms.print_terms(list_terms)

#Case of Deexcitation operators
#Deexcitation operators can be defined by the letter D,everything else remain the same
#Notice that we are not using the full_con function here, so it will print all terms, not just fully contracted.
print('case of [[V,D1],T1]')
list_terms=comm(comm(['V2'],['D1'],0),['T1'],1.0)

print_terms.print_terms(list_terms)

#The code has other small things it can do but these are the basics. 

#Check the results in latex_output.txt
