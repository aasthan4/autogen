from tests import ccsd_amplitude as ccsd1
from tests import ccsd_amplitude_prod as ccsd2
from main_tools import commutator as c
#This is a simple test to check that the driver, commutator and product functions are still working fine. 
ccsd1.amplitude()
ccsd2.amplitude()

#vimdiff compare latex_output.txt and ccsdresult2 with the files with the same name in tests/ccsdresult
