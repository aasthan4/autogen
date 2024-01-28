from library import make_op
from library import class_term
from pkg import func_ewt
def general_term(ops):
    dict_ind={}
    list_op,dict_ind=make_op.make_op(ops,dict_ind)
    sum1=[]
    coeff=[]
    op=func_ewt.contractedobj('op',1,1)    
    st=[[op]]
    co=[]
    term=class_term.term(1,sum1,coeff,list_op,st,co)
    term.dict_ind=dict_ind
    term.map_org=list_op
    for item in list_op:
	term.coeff_list.append(item.coeff)
	term.sum_list.extend(item.sum_ind)	
	term.st[0][-1].upper.extend(item.st[0][-1].upper)
	term.st[0][-1].lower.extend(item.st[0][-1].lower)
    print term.st[0][-1].upper
    print term.map_org, term.dict_ind
    return term

