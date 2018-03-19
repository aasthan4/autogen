import copy
from collections import deque

class operator(object):
    def __init__(self, kind, dag, pos, name, st, pair, spin):
        self.kind = kind
        self.dag = dag
        self.pos = pos
        self.name = name
        self.string = st

        self.pair = pair
        self.pos2 = 0
        self.spin = spin
    def __repr__(self):
        return self.name

class contractedobj(object):
    def __init__(self, kind, sign, const):
        self.kind = kind
        self.upper = []
        self.lower = []
        self.sign = sign
        self.const = const
	self.anti = 0
        self.matrix = []
        self.strings=[1,2]
    def __repr__(self):
        return self.upper
    def value(self, mat):
        return 1

class matrix_con(object):
    def __init__(self):
	self.upper=[]
	self.lower=[]
    def make_for(self, u, l):
	for item in u:
	    self.upper.append(u.spin)
	for item in l:
	    self.lower.append(l.spin)

def equality_check(contracted, store):
    count_eq = 0
    flag1=0
    lim_count = len(contracted)
    if len(contracted)==len(store):
	for itema in contracted:
	    for itemb in store:
	        if len(itema)==len(itemb):
		    flag1=0
		    for index in range(len(itema)):
		        if itema[index].pos!=itemb[index].pos:
		            flag1=1
		            #break
		    if flag1==0:
		        count_eq=count_eq+1
		    flag1=0
		    if count_eq == lim_count:
			return 1
    else:
	return 0
index = 0
def arrange(cum_d, cum_n, cum_d_pos, cum_n_pos):
    cum_d
    for index in range(len(cum_d)):
	for item in cum_n:
	    if cum_d[index].pair==item.pos:
		#exchange the terms in pos and main
	        swap_v = cum_n[index]
		pos_item = cum_n.index(item)
		cum_n[index]=item
		cum_n[pos_item] = swap_v

		#exchange positions
		swap_p = cum_n_pos[index]
		pos_item = cum_n_pos.index(item.pos)
		cum_n_pos[index]=item.pos
		cum_n_pos[pos_item] = swap_p
'''
def cummulant(contracted, full_formed, new_list, cumulant_present): 
    if (contracted):
        for item1 in contracted:
            cum_nord = []
            cum_norn = []
            cum_pos = []
            cum_norn1 = []
            cum_norn2 = []
            cum_norn_pos = []
            cum_norn1_pos = []
            cum_norn2_pos = []
            cum_nor_pos = []
            for item2 in item1:
                cum_pos.append(item2.pos)
                if item2.dag == '1':
                    cum_nord.append(item2)
                    cum_nor_pos.append(item2.pos)
            for item2 in item1:
                if item2.dag == '0':
                    if item2.string == 1:
                        cum_norn1_pos.append(item2.pos)
                        cum_norn1.append(item2)
                    else :
                        cum_norn2_pos.append(item2.pos)
                        cum_norn2.append(item2)
            #reverse non daggered from each string and print its name
            cum_norn1.reverse()
            cum_norn2.reverse()             
            cum_norn.extend(cum_norn1)
            cum_norn.extend(cum_norn2)
            #reverse nondaggered from each string and reverse the whole to see the sign
            cum_norn1_pos.reverse()
            cum_norn2_pos.reverse()
            cum_norn_pos.extend(cum_norn1_pos)
            cum_norn_pos.extend(cum_norn2_pos)
            
            arrange(cum_nord, cum_norn, cum_nor_pos, cum_norn_pos)
            cum_norn_pos.reverse()
            cum_nor_pos.extend(cum_norn_pos)
             
            #change operator to str
            cum_d_name = []
            cum_n_name = []
            for item in cum_nord:
                    cum_d_name.append(item.name)
            for item in cum_norn:
                    cum_n_name.append(item.name)
            cumulant_present=1
	    new_list.append('\Lambda^{'+''.join(cum_d_name)+'}_{'+''.join(cum_n_name)+'}')
            #if parity.parity(cum_nor_pos, cum_pos):
            #    sign=sign*(-1)
            full_formed.extend(cum_nor_pos)
	    return cumulant_present
'''

def list_of_excp(degree, i, j):
    excep=[]
    #print "here i amd j are : ", i, j
    if degree == 2:
	a_cum = matrix_con()
	b_cum = matrix_con()
	c_cum = matrix_con()	
	a_cum.upper = [0, 0]
	a_cum.lower = [0, 0]
	b_cum.upper = [0, 1]
	b_cum.lower = [0, 1]
	c_cum.upper = [0, 1]
	c_cum.lower = [1, 0]
	if a_cum.upper[i]!=a_cum.lower[j]:
	    excep.append('a')
            #print "exception a"
	if b_cum.upper[i]!=b_cum.lower[j]:
	    excep.append('b')
            #print "exception b"
	if c_cum.upper[i]!=c_cum.lower[j]:
	    excep.append('c')
            #print "exception c"
	
	return excep
    elif degree ==3 :

        a_cum = matrix_con()
        b_cum = matrix_con()
        c_cum = matrix_con()
        d_cum = matrix_con()
        e_cum = matrix_con()
        f_cum = matrix_con()
        g_cum = matrix_con()
        h_cum = matrix_con()
        i_cum = matrix_con()
        j_cum = matrix_con()


        a_cum.upper=[0,0,0]
        a_cum.lower=[0,0,0]
        b_cum.upper=[0,0,1]
        b_cum.lower=[0,0,1]
        c_cum.upper=[0,0,1]
        c_cum.lower=[0,1,0]
        d_cum.upper=[0,0,1]
        d_cum.lower=[1,0,0]
        e_cum.upper=[0,1,0]
        e_cum.lower=[0,0,1]
        f_cum.upper=[0,1,0]
        f_cum.lower=[0,1,0]
        g_cum.upper=[0,1,0]
        g_cum.lower=[1,0,0]
        h_cum.upper=[1,0,0]
        h_cum.lower=[0,0,1]
        i_cum.upper=[1,0,0]
        i_cum.lower=[0,1,0]
        j_cum.upper=[1,0,0]
        j_cum.lower=[1,0,0]


        if a_cum.upper[i]!=a_cum.lower[j]:
            excep.append('a')
            print "exception a"
        if b_cum.upper[i]!=b_cum.lower[j]:
            excep.append('b')
            print "exception b"
        if c_cum.upper[i]!=c_cum.lower[j]:
            excep.append('c')
            print "exception c"
        if d_cum.upper[i]!=d_cum.lower[j]:
            excep.append('d')
            print "exception d"
        if e_cum.upper[i]!=e_cum.lower[j]:
            excep.append('e')
            print "exception e"
        if f_cum.upper[i]!=f_cum.lower[j]:
            excep.append('f')
            print "exception f"
        if g_cum.upper[i]!=g_cum.lower[j]:
            excep.append('g')
            print "exception g"
        if h_cum.upper[i]!=h_cum.lower[j]:
            excep.append('h')
            print "exception h"
        if i_cum.upper[i]!=i_cum.lower[j]:
            excep.append('i')
            print "exception i"
        if j_cum.upper[i]!=j_cum.lower[j]:
            excep.append('j')
            print "exception j"
        
        if excep:
            print excep
        return excep

    else :
	return excep
def sub_1D(mat1, mat2):
    if len(mat1)==len(mat2):
        for i in range(len(mat1)):
            mat1[i]=mat1[i]-mat2[i]
        return mat1
    else:
        print "error:matrix of uneven length in addition_matrix function"
def addition_matrix(degree, exceptions):
    matrix = []
    const = 1.0
    if degree == 2:
	matrix = [2, -2]
	for item in exceptions :
	    if item == 'a':
		matrix[0]-=1
		matrix[1]+=1
	    elif item == 'b':
		matrix[0]-=2
		matrix[1]-=1
	    elif item == 'c':
		matrix[0]+=1
		matrix[1]+=2
	#find GCF : not necessary in degree 2
        #print "here is the matrix of exceptions", matrix
	const = 2.0/6.0
	if matrix[1]==0 and matrix[0]!=0:
	    const=const*matrix[0]
	    matrix[0]=1
    elif degree ==3:
        matrix = [-2,-2,-2,-6,-6,-6]
        for item in exceptions:

            if item == 'a':
                matrix = sub_1D(matrix, [1,1,1,0,0,0])
            if item == 'b':
                matrix = sub_1D(matrix, [1,-1,-1,-2,0,0])
            if item == 'c':
                matrix = sub_1D(matrix, [-1,-1,1,0,0,-2])
            if item == 'd':
                matrix = sub_1D(matrix, [-1,1,-1,0,-2,0])
            if item == 'e':
                matrix = sub_1D(matrix, [-1,1,-1,0,0,-2])
            if item == 'f':
                matrix = sub_1D(matrix, [1,-1,-1,0,-2,0])
            if item == 'g':
                matrix = sub_1D(matrix, [-1,-1,1,-2,0,0])
            if item == 'h':
                matrix = sub_1D(matrix, [-1,-1,1,0,-2,0])
            if item == 'i':
                matrix = sub_1D(matrix, [-1,1,-1,-2,0,0])
            if item == 'j':
                matrix = sub_1D(matrix, [1,-1,-1,0,0,-2])
            print "matrix ", matrix
    return const, matrix
def cummulant(contracted, full_formed, new_list, con_spin_upper, con_spin_lower):

    object_cumulant = []  
    #print "entered cumulant for loop", contracted
    
    const = 1.0
    if (contracted):

        #before storing the spin, make the spin of all the contractions equal. 
        #This is needed to sum the small lambdas to capital lambdas


        for item1 in contracted:

            cum_nord = []
            cum_norn = []
            cum_pos = []
            cum_norn1 = []
            cum_norn2 = []
            cum_norn_pos = []
            cum_norn1_pos = []
            cum_norn2_pos = []
            cum_nor_pos = []
            for item2 in item1:
                cum_pos.append(item2.pos)
                if item2.dag == '1':
                    cum_nord.append(item2)
                    cum_nor_pos.append(item2.pos)
            for item2 in item1:
                if item2.dag == '0':
                    if item2.string == 1:
                        cum_norn1_pos.append(item2.pos)
                        cum_norn1.append(item2)
                    else :
                        cum_norn2_pos.append(item2.pos)
                        cum_norn2.append(item2)
            #reverse non daggered from each string and print its name
            cum_norn1.reverse()
            cum_norn2.reverse()             
            cum_norn.extend(cum_norn1)
            cum_norn.extend(cum_norn2)
            #reverse nondaggered from each string and reverse the whole to see the sign
            cum_norn1_pos.reverse()
            cum_norn2_pos.reverse()
            cum_norn_pos.extend(cum_norn1_pos)
            cum_norn_pos.extend(cum_norn2_pos)
            
            arrange(cum_nord, cum_norn, cum_nor_pos, cum_norn_pos)
            cum_norn_pos.reverse()
            cum_nor_pos.extend(cum_norn_pos)


	    
	    #make matrix of contraction of cummulant
	    cum_spin=matrix_con()
            cum_d_spin = []
            cum_n_spin = []
	    #make the try full contracted term to be returned as object cumulant
	    #print "Inside cumulant ------trying to make the object\n"


    
            for item in cum_nord:
                    cum_d_spin.append(item.spin)
            for item in cum_norn:
                    cum_n_spin.append(item.spin)
            #change the spin of the operators which are contracted already
            
            for i in range(len(cum_d_spin)):
                #print "in the loop of spin correction", con_spin_upper, con_spin_lower,"\n"
                for j in range(len(con_spin_lower)):
                    if cum_d_spin[i] == con_spin_lower[j] :
                        #print "item found----", cum_d_spin[i], con_spin_lower[j]
                        cum_d_spin[i] = min(con_spin_lower[j], con_spin_upper[j])
            for i in range(len(cum_n_spin)):
                #print "in the loop of spin correction", con_spin_upper, con_spin_lower,"\n"
                for j in range(len(con_spin_upper)):
                    if cum_n_spin[i] == con_spin_upper[j] :
                        #print "item found----", cum_n_spin[i], con_spin_upper[j]
                        cum_n_spin[i] = min(con_spin_lower[j], con_spin_upper[j])
            
            cum_spin.upper = cum_d_spin
	    cum_spin.lower = cum_n_spin

	    #print "Here is the cumulant spin list", cum_spin.upper, cum_spin.lower
            exceptions = [] #the list of the terms that do not follow the condition of the 
	    #conditions for the degree of cummulant
	    degree_cum=len(cum_spin.upper)
	    #store the terms whose summition is not required: small lambdas [01][10] kind of
	    for i in range(len(cum_spin.upper)) :
		for j in range(len(cum_spin.lower)):
		    if cum_spin.upper[i]==cum_spin.lower[j]:

                        #print "There is an exception generated in cumulant spin :", cum_spin.lower, cum_spin.upper
			exceptions.extend(list_of_excp(degree_cum, i, j))
             
	    #do the addition matrix

            #print "These are the spin of the cumulant ----------", cum_spin.lower, cum_spin.upper
	    const, value_mat = addition_matrix(degree_cum, set(exceptions))
	    #make the object for full contraction
	    try_full_con1=contractedobj('l', 1, 1)

	    #print "Inside cumulant ------", try_full_con1.kind
	    try_full_con1.upper = cum_nord
	    try_full_con1.lower = cum_norn
	    #if there is an anti term in the lambda:
            
            if value_mat and value_mat[1]!=0:
		try_full_con1.anti=1
            #store the matrix in the contracted object
            try_full_con1.matrix = value_mat

	    #BY FORCE MAKE NON ANTI
	    #try_full_con1.anti = 0
	    #if value_mat:
	    #    value_mat[0]=1.0
	    #    value_mat[1]=0.0
	    #const = 1.0



	    object_cumulant.append(try_full_con1) # if total number of cumulants are not being added : LOOK HERE
	    #print "\n\nconstand and matrix = ", const, value_mat, exceptions
            #change operator to str
            cum_d_name = []
            cum_n_name = []
            for item in cum_nord:
                    cum_d_name.append(item.name)
            for item in cum_norn:
                    cum_n_name.append(item.name)
	    if value_mat:
	        new_list.append('(')
	        if value_mat[0]==1:


	    	    new_list.append('\Lambda^{'+''.join(cum_d_name)+'}_{'+''.join(cum_n_name)+'}')
	        elif value_mat[0]>1:

	    	    new_list.append(str(value_mat[0])+'\Lambda^{'+''.join(cum_d_name)+'}_{'+''.join(cum_n_name)+'}')
	        if value_mat[0]!=0 and value_mat[1]!=0 and value_mat[1]!=-1:
		    new_list.append('+')
		cum_n_name.reverse()
	        if value_mat[1]==1:
	    	    new_list.append('\Lambda^{'+''.join(cum_d_name)+'}_{'+''.join(cum_n_name)+'}')
	        elif value_mat[1]==-1:
	    	    new_list.append('-'+'\Lambda^{'+''.join(cum_d_name)+'}_{'+''.join(cum_n_name)+'}')
	        elif abs(value_mat[1])>1:
	    	    new_list.append(str(value_mat[1])+'\Lambda^{'+''.join(cum_d_name)+'}_{'+''.join(cum_n_name)+'}')
		new_list.append(')')
	    else :
		
	    	new_list.append('\Lambda^{'+''.join(cum_d_name)+'}_{'+''.join(cum_n_name)+'}')
		
            #if parity.parity(cum_nor_pos, cum_pos):
            #    sign=sign*(-1)
            full_formed.extend(cum_nor_pos)
    return const, object_cumulant
	    
def normal_order(full, output, output_pos, full_formed):
    for item1 in full:
        if item1.dag=='1' and item1.string == 1:
            output.append(item1)
            output_pos.append(item1.pos)

	    #print "added\n"
    for item1 in full:
        if item1.dag=='1' and item1.string == 2:
            output.append(item1)
            output_pos.append(item1.pos)
	    #print "added\n"
    for item1 in full:
        if item1.dag=='0' and item1.string == 2:
            output.append(item1)
            output_pos.append(item1.pos)
	    #print "added\n"
    for item1 in full:
        if item1.dag=='0' and item1.string == 1:
            output.append(item1)
            output_pos.append(item1.pos)
	    #print "added\n"
    full_formed.extend(output_pos)
    #print "Inside normal order function : full formed : ", full_formed
'''
def write_normal_order(new_list, output):
    new_list.append('\\{')
    for item in output:
        if item.dag=='1' and item.string==1:
            tmp_4 = 'a^+_{'+item.name+'}'
            new_list.append(tmp_4)
    for item in output :
        if ( item.dag=='1') and item.string ==2:
            tmp_4 = 'a^+_{'+item.name+'}'
            new_list.append(tmp_4)
    for item in output:
        if item.dag=='0' and item.string==2:
            tmp_4 = 'a_{'+item.name+'}'
            new_list.append(tmp_4)
    for item in output :
        if ( item.dag=='0') and item.string ==1:
            tmp_4 = 'a_{'+item.name+'}'
            new_list.append(tmp_4)
    new_list.append('\\}')
'''
#------------changed in order to print in the form of E(abc)(efg)
def write_normal_order(new_list, output):
    new_list.append('\\{E^{')
    for item in output:
        if item.dag=='1' and item.string==1:
            tmp_4 = item.name

            new_list.append(tmp_4)
    for item in output :
        if ( item.dag=='1') and item.string ==2:
            tmp_4 = item.name
            new_list.append(tmp_4)
    new_list.append('}_{')
    for item in reversed(output):
	#remember here the 1st string comes first as in writig in E has different rules than straight 
        if item.dag=='0' and item.string==1:
	    #print "item name is ", item.name
            tmp_4 = item.name
	    new_list.append(tmp_4)
    for item in reversed(output) :
        if ( item.dag=='0') and item.string ==2:
	    
	    #print "item name is ", item.name
            tmp_4 = item.name
	    new_list.append(tmp_4)
    new_list.append('}\\}')
def normal_order_adv(full, output):
    for item1 in full:
        flag=0
        for item2 in output:
            if item1.pos==item2.pos:
                flag=1
        if (not flag) and (item1.dag=='1') and item1.string ==1:
            output.append(item1)
    for item1 in full:
        flag=0
        for item2 in output:
            if item1.pos==item2.pos:
                flag=1
        if (not flag) and (item1.dag=='1') and item1.string==2:
            output.append(item1)
    for item1 in full:
        flag=0
        for item2 in output:
            if item1.pos==item2.pos:
                flag=1
        if (not flag) and (item1.dag=='0') and item1.string ==2:
            output.append(item1)
    for item1 in full:
        flag=0
        for item2 in output:
            if item1.pos==item2.pos:
                flag=1
        if (not flag) and (item1.dag=='0') and item1.string==1:
            output.append(item1)

def check_for_same_contraction(spin_list_upper, spin_list_lower, counter):
    if spin_list_lower[counter]==spin_list_upper[counter]:
        '''
	garbage=spin_list_upper[counter]
        spin_list_upper.remove(garbage)
        spin_list_lower.remove(garbage)
        counter=0
        loop_start=spin_list_upper[counter]	
	'''

def loop_present1(spin_list_upper, spin_list_lower, loop_start, counter):
    #print spin_list_upper, spin_list_lower, 'here are the spins'
    if not spin_list_upper:
        #print "spin list empty"
        return 0.0
    if loop_start==-1:
        #print "loop start executed"
        loop_start=spin_list_upper[counter]
    if spin_list_upper[counter]==spin_list_lower[counter]:
        #print "found acon contraction"
        spin_list_upper.remove(spin_list_upper[counter])
        spin_list_lower.remove(spin_list_lower[counter])
	loop_start = -1
	#print 'con removed'
	if not spin_list_upper:
	    return 0.0
    else :
        if spin_list_lower[counter]==loop_start:
            #print "congratulations the loop present worked"
            return 1.0
        found_match=0
        for item in spin_list_upper:
            if item==spin_list_lower[counter]:
                found_match=1
                spin_list_upper.remove(spin_list_upper[counter])
                spin_list_lower.remove(spin_list_lower[counter])
                for i in range(len(spin_list_upper)):
                    if spin_list_upper[i]==item:
                        counter=i
                #print "cunter new = ", counter
                return loop_present1(spin_list_upper, spin_list_lower, loop_start, counter)
        if found_match==0:
            #print "not found in upper spin, deleting"
            spin_list_upper.remove(spin_list_upper[counter])
            spin_list_lower.remove(spin_list_lower[counter])
            return loop_present1(spin_list_upper, spin_list_lower, -1, 0)
def loop_present(spin_list_upper, spin_list_lower, loop_start, counter):
    loopcount=0.0
    while spin_list_upper:
	#print 'loop_present while loop executed'
	loopcount+=loop_present1(spin_list_upper, spin_list_lower, loop_start, counter)
    return loopcount

def make_operators_single(string1, string2, str_no, p):
    overall=deque([])
    

    for item in string1:
        if item>='i' and item<='n':
	    x=operator('ho', '1', p+1, item, str_no, -1, 0)
	    overall.append(x)
	    p+=1
        elif item>='u' and item<='z':
            x=operator('ac', '1', p+1, item, str_no, -1, 0)
            overall.append(x)
	    p+=1

        elif item >='a' and item<='h':
	    x=operator('pa', '1', p+1, item, str_no, -1, 0)
	    overall.append(x)
	    p+=1
        elif item >='p' and item<='s':
	    x=operator('ge', '1', p+1, item, str_no, -1, 0)
	    overall.append(x)
	    p+=1
    
    for item in reversed(string2):
        if item>='i' and item<='n':
	    x=operator('ho', '0', p+1, item, str_no, -1, 0)
	    overall.append(x)
	    p+=1
        elif item>='u' and item<='z' or item=='o' or item == 't':
            x=operator('ac','0', p+1, item, str_no, -1, 0)
            overall.append(x)
	    p+=1

        elif item >='a' and item<='h':
	    x=operator('pa', '0', p+1, item, str_no, -1, 0)
	    overall.append(x)
	    p+=1
        elif item >='p' and item<='s':
	    x=operator('ge', '0', p+1, item, str_no, -1, 0)
	    overall.append(x)
	    p+=1
    return overall
def make_operators(holes, active, particles):
    overall_i=deque([])
    overall_a=deque([])
    overall_u=deque([])
    p=0

    for item in holes:
	x=operator('ho', -1, p+1, item, 0, -1, 0)
	overall_i.append(x)
	p+=1
    for item in active:
	x=operator('ac', -1, p+1, item, 0, -1, 0)
	overall_u.append(x)
	p+=1
    for item in particles:
	x=operator('pa', -1, p+1, item, 0, -1, 0)
	overall_a.append(x)
	p+=1
    return overall_i, overall_u, overall_a
#evaluate functioon only evaluates till lambda 2 nnot higher degree lambda
def multiply_cum_matrix(tmp_lambda, mul_mat):
    print " matrix multiplied"
def evaluate(full_con, const_con, gamma_sin, eta_sin, lambda2, lambda3=None):
    if lambda3 is None:
        lambda3=[]
    val = 1.0
    val_expr = 0.0
    print full_con
    for i in range(len(full_con)):
	val=1.0
	for j in range(len(full_con[i])):
	    if full_con[i][j].kind == 'd':
		up = full_con[i][j].upper
		lo = full_con[i][j].lower
		#print up[0].spin, lo[0].spin
		if up[0].name != lo[0].name or up[0].kind != lo[0].kind :
		    val = 0.0
		#print 'delta va; - ', val, full_con[i][j].upper, full_con[i][j].lower
	    if full_con[i][j].kind == 'g':

		up = full_con[i][j].upper
		lo = full_con[i][j].lower
		val = val*gamma_sin[int(up[0].name)][int(lo[0].name)]
		print 'valueof gamma : ', val

                print 'gamma va;upper;lower:- ', gamma_sin[int(up[0].name)][int(lo[0].name)], full_con[i][j].upper, full_con[i][j].lower
	    elif full_con[i][j].kind == 'e':
		up = full_con[i][j].upper
		lo = full_con[i][j].lower
		val = val*eta_sin[int(up[0].name)][int(lo[0].name)]
		print 'value of eta :',val
		#print 'eta va; - ', gamma_sin[int(up[0].name)][int(lo[0].name)], full_con[i][j].upper, full_con[i][j].lower, const_con[i][0], const_con[i][1]

	    elif full_con[i][j].kind == 'l':
		
                #cumulants of rank 2
		if len(full_con[i][j].upper)==2:
                    tmp_mat= lambda2
		    val_tmp = 0.0
		    for item in full_con[i][j].upper:
		        #print 'lambda index upper', item.name
		        tmp_mat = tmp_mat[int(item.name)]
		    for item in full_con[i][j].lower:
		        #print 'lambda index lower', item.name
		        tmp_mat = tmp_mat[int(item.name)]
		    #print '1st lambda', tmp_mat, full_con[i][j].upper, full_con[i][j].lower
		    val_tmp += tmp_mat*full_con[i][j].matrix[0]

		    #print 'value of 1st lambda', val_tmp	
		    if full_con[i][j].anti==1:
			tmp_mat1=copy.copy(lambda2)
			for item1 in full_con[i][j].upper:
		            #print 'lambda index upper', item.name
		            tmp_mat1 = tmp_mat1[int(item1.name)]

			    #print 'entered this matrix for labda', tmp_mat1
		        for item1 in reversed(full_con[i][j].lower):
		            #print 'lambda index lower', item.name
		            tmp_mat1 = tmp_mat1[int(item1.name)]
			    #print 'entered this matrix for labda', tmp_mat1
		        val_tmp += tmp_mat1*full_con[i][j].matrix[1]
		        #print 'value after 2nd lambda', val_tmp	
			#print 'case of 2 lambda values :', tmp_mat1, full_con[i][j].upper, full_con[i][j].lower
		    print 'final value of lambda :',val_tmp
		    #print 'this is the lambda matrix', lambda2

		if len(full_con[i][j].upper)==3:
                    tmp_mat=lambda3
                    #remember to store the value in val_tmp. and divide by 12.
                    tmp_mat=lambda3
                    for item in full_con[i][j].upper:
                        tmp_mat=tmp_mat[int(item.name)]

                    lower_mat = full_con[i][j].lower
                    val_tmp += multiply_cum_matrix(tmp_mat, full_con[i][j].matrix)
                    
		val = val*val_tmp
	#print 'in the evaluate per term loop', val_expr, " + ", val, const_con[i][0], const_con[i][1]
	val_expr += val*const_con[i][0]*const_con[i][1]
	print 'val expression', val_expr
    return val_expr
