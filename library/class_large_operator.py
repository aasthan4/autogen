class large_operator(object):
    def __init__(self,name, fac, sum_ind, coeff, st, co):
        self.name=name
        self.fac=fac
        self.sum_ind=sum_ind
        self.coeff=coeff
        self.st=st
        self.co=co
        self.map_org=[]
    def __repr__(self):
        return self.name

