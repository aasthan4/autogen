from main_tools import product as math
from library import convert_pqr  
import main_tools
from library import pick
from library import print_terms
from library import rn_comm
list_terms=math.prod(['V2'],['T2'],1)
list_terms=convert_pqr.convert_pqr(list_terms)
list_terms=print_terms.clean_list(list_terms)
#list_terms=pick.pick(list_terms, ['i'],['j'])
print '------'
print_terms.print_terms(list_terms)
print '------'
#for item in list_terms:
#    print rn_comm.rank(item)

#list_terms=rn_comm.select_r(list_terms)

#print_terms.print_terms(list_terms)

