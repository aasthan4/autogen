import eq8
import string
import numpy as np
import copy
class term(object):
    def __init__(self, fac, sum_list, coeff_list,lol, st, co):
        self.fac=fac
        self.sum_list=sum_list
        self.coeff_list=copy.deepcopy(coeff_list)
        self.large_op_list=copy.deepcopy(lol)
        self.st=st
        self.co=co
        self.map_org=[]
	self.dict_ind={}
        self.imatrix=np.zeros((len(coeff_list),len(coeff_list)))
        self.amatrix=np.zeros((len(coeff_list),len(coeff_list)))
    def compress(self):
	for term in self.st:
            for op in term:
                if op.kind=='d':
                    if op.upper[0].name>='p' and op.upper[0].name<='s':
                        #find name in coeff
                        self.coeff_list=[[w.replace(op.upper[0].name, op.lower[0].name) for w in l] for l in self.coeff_list]
                        self.sum_list.remove(op.upper[0].name)

                    elif op.lower[0].name>='p' and op.lower[0].name<='s':


                        self.coeff_list=[[w.replace(op.lower[0].name, op.upper[0].name) for w in l] for l in self.coeff_list]
                        self.sum_list.remove(op.lower[0].name)
                    elif (op.upper[0].name in self.sum_list) and (op.lower[0].name in self.sum_list):

                        if op.upper[0].name>=op.lower[0].name:
                            self.coeff_list=[[w.replace(op.upper[0].name, op.lower[0].name) for w in l] for l in self.coeff_list]
                            self.sum_list.remove(op.upper[0].name)
                        elif op.upper[0].name<op.lower[0].name:
                            self.coeff_list=[[w.replace(op.lower[0].name, op.upper[0].name) for w in l] for l in self.coeff_list]
                            self.sum_list.remove(op.lower[0].name)

                    elif op.lower[0].name in self.sum_list:
                        self.coeff_list=[[w.replace(op.lower[0].name, op.upper[0].name) for w in l] for l in self.coeff_list]
                        self.sum_list.remove(op.lower[0].name)
                    elif op.upper[0].name in self.sum_list:
                        self.coeff_list=[[w.replace(op.upper[0].name, op.lower[0].name) for w in l] for l in self.coeff_list]
                        self.sum_list.remove(op.upper[0].name)


    def compare(self, term2):
        '''
        for (c1,c2, t) in zip(self.coeff_list, term2.coeff_list, self.map_org):
            num=1.0
            if t[1]=='2' and t[0]!='X':
                #print self.coeff_list[1], term2.coeff_list[1]

                num=num*eq82.eq82(c1,c2, self, term2)
            elif t[1]=='1' and t[0]!='X':
                num=num*eq82.eq81(c1, c2, self, term2)
        else :
            return num
        '''
        num=1.0




        for (c1, t1) in zip(self.coeff_list,  self.map_org):
            flag=0
            #print t1
            for (c2, t2) in zip(term2.coeff_list, self.map_org):
                #print t2
                if t1[1]==t2[1] and t1[0]==t2[0] and t1[0]!='X':

                    if t1[1]=='2' and eq8.eq8(c1,c2,self,term2):
                        num=num*eq8.eq8(c1,c2,self,term2)
                        flag=1
                        break
                    elif t1[1]=='1' and eq8.eq8(c1,c2,self,term2):
                        num=num*eq8.eq8(c1,c2,self,term2)
                        flag=1
                        break
                elif t1[0]=='X':
                    flag=1
                    break
            if flag==0:
                #print "case to study is happening"
                return 0
        #return num

        if (self.fac*term2.fac)<0 and num!=0:
            print num, '-1'
            return -1
        elif (self.fac*term2.fac)>0 and num!=0:
            print num, '1'
            return 1
        else :
            print num, '0'
            return 0

    #algorithm to condition that each contraction should have 1 end to H
    #once reach H, store coeff of H in ind
    #store all other Ts in map_org
    #from dict and mapping, locate all ends of contraction
    #check whether all operators are in mapping
    def cond_cont(self,dict_ind):
        flag=0
        map_org=[]
        maping=[]
        for item in self.large_op_list:
            if item.name[0]=='T' or item.name[0]=='D':
                map_org.append(item)
            if item.name=='F1' or item.name=='V2':
                ind=self.large_op_list.index(item)
                #flag=1
        for item in self.coeff_list[ind]:
            maping.append(dict_ind[item])
        for item in map_org:
            if item.name not in maping:
                self.fac=0.0
        #self.map_org=map_org
        #self.build_map_org()
    def isa(self,x):

        if x>='a' and x<='h':
            return 1

        elif len(x)==2 and x[0]>='a' and x[0]<='h':
            return 1
        else: 
	    return 0
    def isi(self,x):
        if x>='i' and x<='n':
            return 1
        elif len(x)==2 and x[0]>='i' and x[0]<='n':
            return 1
        else:
            return 0
    def isp(self,x):
	if x>='p' and x<='t':
	    return 1
        elif len(x)==2 and x[0]>='p' and x[0]<='t':
            return 1
	else :
	    return 0
    def is_dummy(self, x):
        if x in self.sum_list:
            return 1
        else :
            return 0
    def type(self,x):
        if self.isa(x):
            return 'a'
        elif self.isi(x):
            return 'i'
	elif self.isp(x):
	    return 'p'


    def cpre_cstm(self,term2,a,b):
        for i,j in zip(a,b):
            flag1=0
            #print a,b
            #print i,self.sum_list,j,term2.sum_list
            if i in self.sum_list and j in term2.sum_list:

                if self.isi(i) and self.isi(j):
                    flag1=1
                elif self.isa(i) and self.isa(j):
                    flag1=1
                else:
                    return 0
            #elif i not in self.sum_list or j not in self.sum_list:
                #return 0
            elif i==j:
                flag1=1
            else :
                return 0

            #print i,j, flag1
        return 1
    def mapping(self):
        map1=[]
        for item in self.large_op_list:
            map1.append(item.name)
        self.map_org=map1
    def dummy_check(self, term2):
        count_eql=0
        flag2=0
        #print self.map_org
        for i in self.map_org:
            flag=0
            #print 'self',i
            for j in term2.map_org:
                #print 'matching', j
                if i[0]==j[0] and i[1]==j[1] and flag==0 and i[0]!='X' and j[0]!='X':
                    ind1=self.map_org.index(i)
                    ind2=self.map_org.index(j)

                    if self.cpre_cstm(term2,self.coeff_list[ind1], term2.coeff_list[ind2]):
                        count_eql+=1
                        flag=1
                        #print 'match',j, count_eql
            if flag==0:
                flag2=1
                        #continue
        if count_eql==(len(self.map_org)-1):
        #if flag2==0:
            #print "changing"
            self.fac+=term2.fac
            term2.fac=0.0

    def print_term(self):
        print self.fac,
        print 'Sum', self.sum_list,
        for i in range(len(self.large_op_list)):
	    if self.large_op_list[i].name[0]!='X':
                print self.large_op_list[i].name[0],self.coeff_list[i],
	if self.st[0][-1].kind=='op':

	    print 'E^',self.st[0][-1].upper,'_',self.st[0][-1].lower,
        print '\n',
    def print_latex(self, f):
        #f=open('exp_out_latex.txt','a')
        f.write(str(self.fac))
        if self.sum_list:
            f.write("\sum_{")
            for item in self.sum_list:
                f.write(item+' ')
            f.write("}")
        for i in range(0,len(self.large_op_list)):
            if self.large_op_list[i].name[0]!='V' and self.large_op_list[i].name[0]!='X':
                f.write(self.large_op_list[i].name[0])
                f.write("^{")

            elif self.large_op_list[i].name[0]=='V':
                f.write("<")

            if self.large_op_list[i].name[0]!='X':
                for it1 in range(0,len(self.coeff_list[i])/2):
                    f.write(self.coeff_list[i][it1])

            if self.large_op_list[i].name[0]!='V' and self.large_op_list[i].name[0]!='X':
                f.write("}_{")
            elif self.large_op_list[i].name[0]=='V':
                f.write("||")

            if self.large_op_list[i].name[0]!='X':
                for it2 in range(len(self.coeff_list[i])/2, len(self.coeff_list[i])):
                    f.write(self.coeff_list[i][it2])
            if self.large_op_list[i].name[0]!='V' and self.large_op_list[i].name[0]!='X':
                f.write("}")
            elif self.large_op_list[i].name[0]=='V':
                f.write(">")
	if self.st[0][-1].kind=='op':
	    f.write("E^{")
            for it1 in self.st[0][-1].upper:
                f.write(it1)
	    f.write("}_{")
            for it1 in self.st[0][-1].lower:
                f.write(it1)
	    f.write("}")
	
        f.write('\\\\ \n')

    def build_map_org(self):
	for item in self.large_op_list:
	    self.map_org.append(item)





