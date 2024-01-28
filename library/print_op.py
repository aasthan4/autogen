
def print_op(st, co):
    for term,pre in zip(st,co):
        tmp=str(pre[0])#*pre[1))
        for op in term:
            if op.kind=='d':
                tmp=tmp+'\delta_{'+str(op.upper)+str(op.lower)+'}'
            elif op.kind=='op':
                tmp=tmp+'\{E^{'+str(op.upper)+'}'+'_'+'{'+str(op.lower)+'}\}'
        tmp=tmp+'\\\\'
        print(tmp)
