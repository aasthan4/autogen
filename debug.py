from main_tools import product as math
from library import convert_pqr  
import main_tools
from library import pick
from library import print_terms
list_terms=math.prod(['V2'],['T2'],1)
list_terms=convert_pqr.convert_pqr(list_terms)
list_terms=pick.pick(list_terms, ['i'],['j'])
print '------'
print_terms.print_terms(list_terms)

