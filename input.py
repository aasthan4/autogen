from tests import ccsd_amplitude as ccsd

from main_tools import commutator as math1
from main_tools import product as math2
from library import full_con
import library
#ccsd.amplitude()
list=math2.prod(['V2'],['T2'],1)
library.print_terms.print_terms(full_con.full_con_terms(list))
