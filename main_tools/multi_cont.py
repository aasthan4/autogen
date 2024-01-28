import pkg.func_ewt as func_ewt
import pkg.fewt as fewt
import copy
import library.make_op as make_op
import library.print_op as p_op
import library.full_con as full_con
'''
Problems :
    1. the fully uncontrancted expression has wrong ordering in the lower half.
    2. look at fewt there is a problem with adding general states in line 298

'''

#make operators
#X, V, T1 = make_op.make_op()

'''
op1=func_ewt.contractedobj('op', 1, 1)
op1.upper=['i','j']
op1.lower=['a','b']
op3=func_ewt.contractedobj('op', 1, 1)
op3.upper=['p','q']
op3.lower=['r','s']
op2=func_ewt.contractedobj('op', 1, 1)
op2.upper=['c']
op2.lower=['k']
st1=[[op1]]
st2=[[op2]]
stp=[[op3]]
'''
def sp_multi(a,b):
    re=[]
    #print a, b
    for item1, item2 in zip(a,b):
        item3=item1*item2
        re.append(item3)
    return re
def arrange(st, co, new_term_half, new_const_half):
    terms=[]
    const=[]
    tmp_term=[]
    #print 'in arrange', st, new_term_half
    for term, pre in zip(st, co):
        tmp_term = copy.deepcopy(new_term_half)
        tmp_term.extend(term)
        tmp_const=sp_multi(pre,new_const_half)
        #print tmp_const
        terms.append(tmp_term)
        const.append(tmp_const)
    #print "after arrange",terms, const
    return terms, const
#assumption : last part of a tern is the working 'op'. 'op' cannot be before any 'de'
def multi_cont(st1, st2, const1, const2):
    flag2=0
    final_terms=[]
    final_const=[]
    #print 'first operator string constant',const1
    for (term1, pre1) in zip(st1, const1):
        new_term_half=[]
        for op11 in term1:
            if op11.kind!='op':
                new_term_half.append(op11)
        for term2, pre2 in zip(st2, const2):
            for op22 in term2:
                if op22.kind!='op':
                    new_term_half.append(op22)
                elif op11.kind=='op':
                    flag2=1
                    new_const_half=sp_multi(pre1,pre2)
                    o,c=fewt.ewt(op11.upper, op11.lower, op22.upper, op22.lower)
                    terms, const=arrange(o,c, new_term_half, new_const_half)
                    final_terms.extend(terms)
                    final_const.extend(const)
                    #p_op.print_op(final_terms,final_const)
                elif op11.kind!='op':
                    new_term_half.append(op22)
                    final_terms.append(new_term_half)
                    final_const.append(sp_multi(pre1,pre2))
                else :
                    print(" there is a case in multi_cont file I am missing")
            flag2=0
    return final_terms, final_const
'''
a,b = multi_cont(X.st, V.st, X.co, V.co)
p_op.print_op(a,b)
print '---------------'

a,b=  multi_cont(a, T1.st, b,T1.co)

a,b=full_con.full_con(a,b)

p_op.print_op(a,b)
'''
