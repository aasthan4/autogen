from main_tools import driv3 as driv2
import main_tools.product as prod
import main_tools.commutator as comm
from library import print_terms 
from library import full_con
#This is a test function which generates all the CCSD amplitude terms. 
#It tests the accuracy of comm and prod functions without including Deexcitations. 
def amplitude():

    list_terms=[]
    print('X1 Terms')
    
    print('X1 F1')

    list_terms.extend(prod.prod(['X1'],['F1'],1.0) )
    print('X1 F1 T1')


    list_terms.extend(prod.prod(['X1'],comm.comm(['F1'],['T1'],0),1.0))
    print('X1 F1 T2')
    list_terms.extend(prod.prod(['X1'],comm.comm(['F1'],['T2'],0),1.0))
    print('X1 F1 T1 T11')

    list_terms.extend(prod.prod(['X1'],comm.comm(comm.comm(['F1'],['T1'],0),['T11'],0),0.5))
    print('X1 F1 T2 T21')
    list_terms.extend(prod.prod(['X1'],comm.comm(comm.comm(['F1'],['T2'],0),['T21'],0),0.5))
    print('X1 F1 T1 T2')
    list_terms.extend(prod.prod(['X1'],comm.comm(comm.comm(['F1'],['T1'],0),['T2'],0),1.0))
    #list_terms=full_con.full_terms(list_terms)
    #print_terms.print_terms(list_terms,'ccsdresult2')
    #list_terms=[]

    print('X1 V2')
    list_terms.extend(prod.prod(['X1'],['V2'],1.0) )
    print('X1 V2 T1')

    list_terms.extend(prod.prod(['X1'],comm.comm(['V2'],['T1'],0),1.0))
    print('X1 V2 T2')
    list_terms.extend(prod.prod(['X1'],comm.comm(['V2'],['T2'],0),1.0))
    print('X1 V2 T1 T11')
    list_terms.extend(prod.prod(['X1'],comm.comm(comm.comm(['V2'],['T1'],0),['T12'],0),0.5))
    print('X1 V2 T2 T21')
    list_terms.extend(prod.prod(['X1'],comm.comm(comm.comm(['V2'],['T2'],0),['T22'],0),0.5))
    print('X1 V2 T1 T2')

    list_terms.extend(prod.prod(['X1'],comm.comm(comm.comm(['V2'],['T1'],0),['T2'],0),1.0))
    print('X1 V2 T1 T11 T12')

    list_terms.extend(prod.prod(['X1'],comm.comm(comm.comm(comm.comm(['V2'],['T1'],0),['T12'],0),['T13'],0),1.0/6.0))

    print('X2 Terms')
    list_terms=full_con.full_terms(list_terms)
    print_terms.print_terms(list_terms,'ccsdresult')
    list_terms=[]
    



    print('X2 F1')
    #driv2.driver(1.0,['X2','F1'])
    list_terms=prod.prod(['X2'],['F1'],1.0)
    print('X2 F1 T1')
    #driv2.driver(1.0,['X2','F1', 'T1'])
    list_terms.extend(prod.prod(['X2'],comm.comm(['F1'],['T11'],0),1.0))
    print('X2 F1 T1 T1')
    #driv2.driver(0.5,['X2','F1', 'T1', 'T11'])
    list_terms.extend(prod.prod(['X2'],comm.comm(comm.comm(['F1'],['T11'],0),['T12'],0),0.5))
    list_terms=full_con.full_terms(list_terms)

    print_terms.print_terms(list_terms,'ccsdresult2')
    list_terms=[]
    print('X2 F1 T2 ')
    #driv2.driver(1.0,['X2','F1', 'T2'])
    list_terms.extend(prod.prod(['X2'],comm.comm(['F1'],['T21'],0),1.0))
    print('X2 F1 T2 T2')
    #driv2.driver(0.5,['X2','F1', 'T2', 'T21'])
    list_terms.extend(prod.prod(['X2'],comm.comm(comm.comm(['F1'],['T21'],0),['T22'],0),0.5))
    list_terms=full_con.full_terms(list_terms)
    print_terms.print_terms(list_terms,'ccsdresult2')
    list_terms=[]
    print('X2 F1 T1 T2')
    #driv2.driver(1.0,['X2','F1', 'T1','T2'])
    list_terms.extend(prod.prod(['X2'],comm.comm(comm.comm(['F1'],['T11'],0),['T22'],0),1.0))
    list_terms=full_con.full_terms(list_terms)
    print_terms.print_terms(list_terms,'ccsdresult2')
    list_terms=[]


    print('X2 V2 T1')
    #driv2.driver(1.0,['X2','V2', 'T1'])
    list_terms.extend(prod.prod(['X2'],comm.comm(['V2'],['T11'],0),1.0))
    print('X2 V2 T1 T2')
    #driv2.driver(0.5,['X2','V2', 'T1', 'T11'])
    list_terms.extend(prod.prod(['X2'],comm.comm(comm.comm(['V2'],['T11'],0),['T12'],0),0.5))
    list_terms=full_con.full_terms(list_terms)
    print_terms.print_terms(list_terms,'ccsdresult2')
    list_terms=[]
    print('X2 V2 T1 T1 T1')
    #driv2.driver(1.0/6.0,['X2','V2', 'T1', 'T11', 'T12'])
    list_terms.extend(prod.prod(['X2'],comm.comm(comm.comm(comm.comm(['V2'],['T11'],0),['T12'],0),['T13'],0),1.0/6.0))
    print('X2 V2 T2')
    #driv2.driver(1.0,['X2','V2','T2'])
    list_terms.extend(prod.prod(['X2'],comm.comm(['V2'],['T21'],0),1.0))
    list_terms=full_con.full_terms(list_terms)
    print_terms.print_terms(list_terms,'ccsdresult2')
    list_terms=[]

    #driv2.driver(0.5,['X2','V2','T2','T21'])
    print('X2 V2 T2 T2')
    list_terms.extend(prod.prod(['X2'],comm.comm(comm.comm(['V2'],['T21'],0),['T22'],0),0.5))
    list_terms=full_con.full_terms(list_terms)
    print_terms.print_terms(list_terms,'ccsdresult2')
    list_terms=[]
    print('X2 V2 T1 T2')
    #driv2.driver(1.0,['X2','V2','T1','T2'])
    list_terms.extend(prod.prod(['X2'],comm.comm(comm.comm(['V2'],['T11'],0),['T22'],0),1.0))
    print('X2 V2 T1 T1 T2')
    #driv2.driver(0.5,['X2','V2','T1','T11','T2'])
    list_terms.extend(prod.prod(['X2'],comm.comm(comm.comm(comm.comm(['V2'],['T11'],0),['T12'],0),['T23'],0),0.5))
    list_terms=full_con.full_terms(list_terms)
    print_terms.print_terms(list_terms,'ccsdresult2')
    list_terms=[]
    print('X2 V2 T1 T1 T1 T1')
    #driv2.driver(1.0/24.0,['X2','V2','T1','T11','T12','T13'])
    list_terms.extend(prod.prod(['X2'],comm.comm(comm.comm(comm.comm(comm.comm(['V2'],['T11'],0),['T12'],0),['T13'],0),['T14'],0),1.0/24.0))

    list_terms=full_con.full_terms(list_terms)

    print_terms.print_terms(list_terms,'ccsdresult2')
   
