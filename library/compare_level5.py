import copy
import class_term
import functions
from pkg import parity
class ind(object):
    def __init__(self, name, seen, parent):
        self.name = name
        self.seen=seen
        self.parent=parent
        self.pair=self


def unsee(coeff):
    for c1 in coeff:
        for i in c1:
            i.seen=0
def find_ind(coeff, i):
    flag2=0
    for c1 in range(len(coeff)):
        for j in range(len(coeff[c1])):
            if coeff[c1][j].seen==0 and coeff[c1][j].name==i.name:
                flag2=1
		#print 'found in find_ind ', coeff[c1][j].name
                return coeff[c1][j],c1,j
    if flag2==0:
        #print 'not found or already seen', i.name
        return 0,-1,-1
def coeff_seen(coeff):
    flag2=1
    for c1 in coeff:
        for i in c1:
            if i.seen==0:
                flag2=0
    return flag2
def swap(c1):
    tmp = c1[2]
    c[2]=c[3]
    c[3]=tmp

def match(term1,term2,i1,i2,nondummy_map):
    #same type:if not dummy, samename: if dummy ok
    if term1.type(i1.name)==term2.type(i2.name):
        '''
        if not term1.is_dummy(i1.name) and not term2.is_dummy(i2.name) and i1.name==i2.name:
	    if i1.name not in nondummy_map:
                #pushing non dummy in dict
	        nondummy_map[i1.name]=i2.name
                return 1
	    elif nondummy_map[i1.name]!=i2.name:
		return 0
        elif not term1.is_dummy(i1.name) and not term2.is_dummy(i2.name) and i1.name!=i2.name:
	    if i1.name not in nondummy_map:
		nondummy_map[i1.name]=i2.name
		return 1
	    elif nondummy_map[i1.name]==i2.name:
		return 1
	    else:
		return 0
        '''
        if not term1.is_dummy(i1.name) and not term2.is_dummy(i2.name) and i1.name==i2.name:
            #they are same move forward
            return 1
            #print 'non dummy match'
        elif term1.is_dummy(i1.name) and term2.is_dummy(i2.name):
            #print 'dummy match'
            return 1
        else :
            return 0
    else :
        return 0


def pick(coeff1, coeff2):
    #print 'length of coeff1',len(coeff1)
    for c1 in reversed(range(0,len(coeff1))):
        '''
        print 'in pick',len(coeff1[c1]), len(coeff2[c1]), coeff1[c1][0].seen,coeff1[c1][1].seen,
        if len(coeff1[c1])==4:
            print coeff1[c1][2].seen,coeff1[c1][3].seen
        else:
            print '\n'
        '''
        if len(coeff1[c1])==2 and len(coeff2[c1])==2 and coeff1[c1][1].seen==0:
            coeff1[c1][1].seen=1
            coeff2[c1][1].seen=1
            return c1,coeff1[c1][1], coeff2[c1][1]
        elif len(coeff1[c1])==4 and len(coeff2[c1])==4:
            if coeff1[c1][2].seen==0:

                coeff1[c1][2].seen=1
                coeff2[c1][2].seen=1
                return c1,coeff1[c1][2], coeff2[c1][2]
            elif coeff1[c1][3].seen==0:

                coeff1[c1][3].seen=1
                coeff2[c1][3].seen=1
                return c1,coeff1[c1][3], coeff2[c1][3]
        elif len(coeff1[c1])==len(coeff2[c1]) and len(coeff1[c1])>4:
	    for i in range((len(coeff1[c1])/2)-1,len(coeff1[c1])):
		if coeff1[c1][i].seen==0:

		    coeff1[c1][i].seen==1
		    coeff2[c1][i].seen==1
		    return c1, coeff1[c1][i], coeff2[c1][i]
    print "something is wrong in picking, see compare function line 48 file in library"
    return -1,0,0

    exit()

#produces all possible permutations of a 4,6,8 index coeff/operator for comparing
# with correct sign
#Algo : simple 1. produce all permutations through functions.permutations
#--------then use the parity.paritty to decide sign and add all up in a list
#--------send it to the levels for comparision.
def juggle(term,pos):
    c=term.coeff_list[pos]

    possible_coeff_tmp=[]
    possible_coeff=[]
    if len(c)==4:
        possible_coeff=[[c[0],c[1],c[3],c[2]],[c[1],c[0],c[3],c[2]],[c[1],c[0],c[2],c[3]],[c[0],c[1],c[2],c[3]]]
    #create all possibilities of terms using permute function
    elif len(c)==6:
	functions.permute(c,3,5,possible_coeff_tmp)
	for item in possible_coeff_tmp:
	    functions.permute(item,3,5, possible_coeff)
	#print 'test that all permutations are created of operators',possible_coeff
	#sys.exit(0)
    tmp_term=copy.deepcopy(term)
    ret_terms=[]
    #create the sign of each term using parity function
    for c1 in possible_coeff:
        tmp_term.fac=term.fac #reinitialize
        tmp_term.coeff_list[pos]=c1
	'''
        if i%2==0:
            tmp_term.fac=term.fac*-1
	'''
	if parity.parity(c1,term.coeff_list[pos])==1:
	    tmp_term.fac=term.fac*-1
	else :
	    tmp_term.fac=term.fac
	#print 'check the sign of terms in juggle', c1,term.coeff_list[pos], parity.parity(c1,term.coeff_list[pos]),"(",tmp_term.fac,term.fac,")"

        ret_terms.append(copy.deepcopy(tmp_term))
    #print ' length og list terms after juggle is :', len(ret_terms)

    return ret_terms


def level1(term1,term2):
    #    Level 1 : same operators (redundant ) and same number of
    #contractions made (E()() also of the same size)
    if len(term1.coeff_list)!=len(term2.coeff_list):
        return 0
    for item1 in term1.map_org:
        flag1=0
        for item2 in term2.map_org:
            if item1.name==item2.name:
                flag1=1
        if flag1!=1:
            return 0
    if len(term1.st[0])!=len(term2.st[0]):

	return 0
    return 1

def level2(term1,term2):
    #type and count of dummy of each type is the same in each coeff
    #just to reduce computaitons
    #Algorithm --
    #
    for c1,t1 in zip(term1.coeff_list, term2.map_org):
        matched=0
        for c2,t2 in zip(term2.coeff_list, term2.map_org):
            if t1.name[0]==t2.name[0] and t1.name[1]==t2.name[1]:
                a1=0
                a2=0
                ii1=0
                ii2=0
                for i1,i2 in zip(c1,c2):
                    if term1.is_dummy(i1):
                        if term1.isa(i1):
                            a1=a1+1
                        else:
                            ii1=ii1+1
                    if term2.is_dummy(i2):
                        if term2.isa(i2):
                            a2=a2+1
                        else:
                            ii2=ii2+1
                if a1==a2 or ii1==ii2:
                    matched=1
        if matched==0:
            return 0
    return 1

def swap(a,b,c):
    tmp=[]
    tmp = a[c]
    a[c]=a[b]
    a[b]=tmp

def heapit(a, size, n,ret):
    if size==1:
        ret.append(copy.deepcopy(a))
        return a
    for i in range(size):
        heapit(a, size-1, n, ret)
        if ((size%2)==1):
            swap(a,0,size-1)
        else:
            swap(a,i,size-1)


    return ret


def level3(term1,term2):
    #create alteranative terms for the symmetry of excitation operators (Ts are the same so can exchange places)
    #VTT- Ts are the same so should be permuted
    #DVT and TVD are not same so D should be permuted separately
    #permutations:

    permute=[]
    ret=[]
    final_terms=[]
    #print term2.coeff_list
    for c2,t2 in zip(term2.coeff_list, term2.map_org):
        if t2.name[0]=='T':
            permute.append(c2)
    #print 'permute list ', permute
    #produce all permuted forms of permute list, through heaps algorithm
    after_permute=heapit(permute, len(permute), len(permute), ret)
    if len(permute)==1:
        after_permute=[after_permute]
    #print 'after permute ', after_permute

    for termx in after_permute:
        tmp_term=[]
        i=0
        for c2,t2 in zip(term2.coeff_list, term2.map_org):
            if t2.name[0]!='T':
                tmp_term.append(c2)
            elif t2.name[0]=='T':
                tmp_term.append(termx[i])
                i=i+1

	if len(term2.coeff_list)!=len(term2.map_org):
           tmp_term.append(term2.coeff_list[-1])#adding the operator coeff----
        x=class_term.term(+1,copy.deepcopy(term2.sum_list), tmp_term, copy.deepcopy(term2.large_op_list),copy.deepcopy(term2.st),copy.deepcopy(term2.co))
        final_terms.append(x)
    permute=[]
    ret=[]
    #print term2.coeff_list
    for c2,t2 in zip(term2.coeff_list, term2.map_org):
        if t2.name[0]=='D':
            permute.append(c2)
    #print 'permute list ', permute
    #produce all permuted forms of permute list, through heaps algorithm
    after_permute=heapit(permute, len(permute), len(permute), ret)
    if len(permute)==1:
        after_permute=[after_permute]
    #print 'after permute ', after_permute

    for termx in after_permute:
        tmp_term=[]
        i=0
        for c2,t2 in zip(term2.coeff_list, term2.map_org):
            if t2.name[0]!='D':
                tmp_term.append(c2)
            elif t2.name[0]=='D':
                tmp_term.append(termx[i])
                i=i+1
	if len(term2.coeff_list)!=len(term2.map_org):
       	    tmp_term.append(term2.coeff_list[-1])#adding the operator coeff----

        x=class_term.term(+1,copy.deepcopy(term2.sum_list), tmp_term, copy.deepcopy(term2.large_op_list),copy.deepcopy(term2.st),copy.deepcopy(term2.co))
        final_terms.append(x)

    return 1, final_terms

#Algo : all possible terms through permutations of a 4index coefficient etc
# are produced. so there will be many forms of the same term in final_terms
#Pitfall : the same terms will also be present when we use jiggle. Jiggle produces
# all permutations of the index inclusing the same index. so a 4 index coeff will
# lead to 5 terms instead of 4. 1 and 2 will be the same.
def level4(term1, term2, final_terms):
    #produce all possibilities of each element coeffcient
    tmp_terms1=[]

    for c2 in range(len(term1.coeff_list)):
        if len(term1.coeff_list[c2])>=4:
            for termx in final_terms:
                if len(termx.coeff_list[c2])>=4:
                    tmp_terms1.extend(juggle(termx,c2))
            final_terms.extend(tmp_terms1)
            tmp_terms1=[]



def go_find(term1,term2,coeff1,coeff2,i1,i2,nondummy_map):
    if match(term1,term2,i1,i2,nondummy_map):
	#print 'in go forward going to find ',i1.name, i2.name
        j1,c1,d1=find_ind(coeff1,i1)
        j2,c2,d2=find_ind(coeff2,i2)
        if j1==0 and j2==0:#both are non dummy

	    #print 'both non dumy'
            return 1
        elif j1==0 or j2==0:#one of them is non dummy

	    #print 'one non dumy'
            return 0
        if c1==c2 and d1==d2:#the position are different
            if j1.seen==0:
                j1.seen=1
            else:
                return 1
            if j2.seen==0:
                j2.seen=1
                return  go_forward(term1,term2,coeff1,coeff2,j1,j2,nondummy_map)
            else:
                return 1
        else :
            return 0

    else:
        return 0


def go_forward(term1,term2,coeff1,coeff2,i1,i2,nondummy_map):
    if match(term1,term2,i1,i2,nondummy_map):
        i1=i1.pair
        i2=i2.pair

	#print 'in go forward going to find ',i1.name, i2.name
        if i1.seen==0:
            i1.seen=1
        else:
            return 1
        if i2.seen==0:
            i2.seen=1
            return  go_find(term1,term2,coeff1,coeff2,i1,i2,nondummy_map)
        else:
            return 1

    else:
        return 0
#Algorithm:
#
#
#
def arrowwork(term1,term2,coeff1, coeff2):
    '''
    print '---e'
    for item1,item2 in zip(coeff1,coeff2):
        for item3 in item1:
            print item3.name,
        print '\n'
        for item4 in item2:
            print item4.name,
        print '\n'
    print '---e'
    '''
    nondummy_map={}
    while not coeff_seen(coeff1):
	#print len(coeff1),len(coeff2)
        c1,i1, i2 =pick(coeff1, coeff2)
	#print 'picked',i1.name, i2.name
        if c1==-1:#case when the 2 coeff are of unequal length
            #print 'cant pick'
            return 0
        if go_forward(term1,term2,coeff1,coeff2,i1,i2, nondummy_map)==0:
            #print 'not going forward'
            return 0
        if go_find(term1,term2,coeff1,coeff2,i1,i2,nondummy_map)==0:
            #print 'not finding'
            return 0
    return 1




def level5(term1, term2, final_terms):
    #map_org becomes immaterial for t2 terms
    #---Algorithm -
    #create indices class objects for each indices in operator such as 'a' in T1(a,k)
    #pair the coefficients to their partners in the indices class of all terms (main terms and copies of term2)
    #arrowwork decides if the two terms are the same and the sign is given by the fac of the term2 copy.
    tmp1=[]
    tmp2=[]
    #build class ind
    for c1 in range(len(term1.coeff_list)):
        for i1 in term1.coeff_list[c1]:
	    if c1==len(term1.map_org):#case when the operator E coeff come up
            	x1=ind(i1,0,'E')
            	tmp1.append(copy.deepcopy(x1))
	    else:
            	x1=ind(i1,0,term1.map_org[c1].name)
            	tmp1.append(copy.deepcopy(x1))

        tmp2.append(copy.deepcopy(tmp1))

        tmp1=[]
    coeff1=copy.deepcopy(tmp2)
    tmp2=[]
    term2_coeffs=[]
    final_coeffs=[]
    #print '---------------------coeff1 length', len(coeff1)
    #build class ind for term2 in final terms
    for termx in final_terms:
        tmp2=[]
        for c2 in range(len(termx.coeff_list)):
            tmp1=[]
            for i2 in termx.coeff_list[c2]:
	        if c2==len(term2.map_org):
                    x2=ind(i2,0,'E')
                    tmp1.append(copy.deepcopy(x2))
		else:
		    #print len(term2.map_org),c2, termx.coeff_list
                    x2=ind(i2,0,term2.map_org[c2].name)
                    tmp1.append(copy.deepcopy(x2))
            tmp2.append(copy.deepcopy(tmp1))
        term2_coeffs.append(copy.deepcopy(tmp2))
    final_coeffs=copy.deepcopy(term2_coeffs)
    #pair the pairs
    for c1 in coeff1:
        #for i1 in c1:
        #    print i1.name
	for ij in range(len(c1)):
	    if ij <len(c1)/2:
	    	c1[ij].pair=c1[ij+len(c1)/2]
	    else :
		c1[ij].pair=c1[ij-len(c1)/2]
    for term2_coeffs in final_coeffs:
        for c1 in term2_coeffs:
            #for i1 in c1:
            #    print i1.name
	    for ij in range(len(c1)):
	    	if ij <len(c1)/2:
	    	    c1[ij].pair=c1[ij+len(c1)/2]
	    	else :
		    c1[ij].pair=c1[ij-len(c1)/2]
    flag=0
    '''
    for item in coeff1:
        for item1 in item:
            print item1.name,
        print '\n'
    print '------'
    '''
    for c2,termx in zip(final_coeffs,final_terms):
        unsee(coeff1)
        unsee(c2)
        #print 'comparing for arrow',term1.coeff_list, termx.coeff_list
        if arrowwork(term1, termx,coeff1, c2)==1:
            flag=termx.fac
            #print 'match', term1.coeff_list, '"',term2.coeff_list,',',termx.coeff_list,',',termx.fac
            break
    return flag


def compare(term1, term2):
    flag=1
    ret=[]
    if flag==1:
        flag=level1(term1,term2)
	#print 'flag level 1 :', flag
    if flag!=0:
        flag=level2(term1,term2)
	#print 'flag level 2 :', flag
    if flag!=0:
        flag, final_terms=level3(term1,term2)
	#print 'flag level 3 :', flag
        #print len(final_terms)
    if flag!=0:
        level4(term1,term2, final_terms)
	#print 'flag level 4 :', flag

        #print len(final_terms)
        #1.include the sign in the face
    if flag!=0:
        #2.return not only 1 but the sign of the face as well.
        flag=level5(term1,term2, final_terms)
	#print 'flag level 5 :', flag
        #print len(final_terms)
    final_terms=[]
    return flag

