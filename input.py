from tests import ccsd_amplitude as ccsd

from main_tools import commutator as math1
from main_tools import product as math2
from library import full_con
from library import convert_pqr
from library import pick
from library import compare_envelope as ce
import library
#ccsd.amplitude()

list_terms=math1.comm(math1.comm(['V2'],['T1'],0),['T1'],1)
list_terms.extend(math1.comm(math1.comm(['V2'],['T1'],0),['D1'],-0.5))
list_terms.extend(math1.comm(math1.comm(['V2'],['D1'],0),['T1'],-0.5))
list_terms.extend(math1.comm(math1.comm(['V2'],['D1'],0),['D1'],1))
list_terms=library.convert_pqr.convert_pqr(list_terms)
list_terms=pick.pick(list_terms,['i'],['j'])
list_terms=ce.compare_envelope(list_terms,1,1)
library.print_terms.print_terms(list_terms)

