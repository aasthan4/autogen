from main_tools import driv3 as driv2
from main_tools import product as pd
from library import print_terms 
def amplitude():


    print('X1 Terms')

    print('X1 F1')
    driv2.driver(1.0,['X1','F1'])
    print('X1 F1 T1')
    driv2.driver(1.0,['X1','F1','T1'])
    print('X1 F1 T2')
    driv2.driver(1.0,['X1','F1','T2'])
    print('X1 F1 T1 T11')
    driv2.driver(0.5,['X1','F1','T1','T11'])
    print('X1 F1 T2 T21')
    driv2.driver(0.5,['X1','F1','T2','T21'])
    print('X1 F1 T1 T2')
    driv2.driver(1.0,['X1','F1','T1','T2'])

    print('X1 V2')
    driv2.driver(1.0,['X1','V2'])
    print('X1 V2 T1')
    driv2.driver(1.0,['X1','V2','T1'])
    print('X1 V2 T2')
    driv2.driver(1.0,['X1','V2','T2'])
    print('X1 V2 T1 T11')
    driv2.driver(0.5,['X1','V2','T1','T11'])
    print('X1 V2 T2 T21')
    driv2.driver(0.5,['X1','V2','T2','T21'])
    print('X1 V2 T1 T2')
    driv2.driver(1.0,['X1','V2','T1','T2'])
    print('X1 V2 T1 T11 T12')
    driv2.driver(1.0/6.0,['X1','V2','T1','T11','T12'])

    print('X2 Terms')


    driv2.driver(1.0,['X2','F1'])
    driv2.driver(1.0,['X2','F1', 'T1'])
    driv2.driver(0.5,['X2','F1', 'T1', 'T11'])
    driv2.driver(1.0,['X2','F1', 'T2'])
    driv2.driver(0.5,['X2','F1', 'T2', 'T21'])
    driv2.driver(1.0,['X2','F1', 'T1','T2'])
    driv2.driver(1.0,['X2','V2', 'T1'])
    driv2.driver(0.5,['X2','V2', 'T1', 'T11'])
    driv2.driver(1.0/6.0,['X2','V2', 'T1', 'T11', 'T12'])
    driv2.driver(1.0,['X2','V2','T2'])
    driv2.driver(0.5,['X2','V2','T2','T21'])

    driv2.driver(1.0,['X2','V2','T1','T2'])
    driv2.driver(0.5,['X2','V2','T1','T11','T2'])
    driv2.driver(1.0/24.0,['X2','V2','T1','T11','T12','T13'])
