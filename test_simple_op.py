from tests import ccsd_amplitude as ccsd
from main_tools.commutator import comm
from library import print_terms
from library import full_con
import time
starttime=time.time()
print 'case of [V,T2]'
list_terms=comm(['V2'],['T2'],1)
print_terms.print_terms(list_terms)
#The following function selects only the fully contracted terms from the above list_terms
#list_terms=full_con.full_terms(list_terms)
#print_terms.print_terms(list_terms)
print "time taken = ", time.time()-starttime
