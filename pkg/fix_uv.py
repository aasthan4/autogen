#This file is the printing part of the whole program. Everthing is being rinted here
#1st part is where contractions are made
#2nd part is where contractions are printed
#3rd partis where there are no contractions and only cummulants and operators are printed.


from collections import deque
import copy
import parity
import func_ewt
import returnop
func=func_ewt
def fix_con(op_no, cnt, lim_cnt, t_list, matched, contracted, contracted_l, contracted_r, a, i, u, full, f, full_pos, i_c, full_con, const_con):
    cnt_tmp=cnt+1 # put condition of limiting cnt
    index = 0
    if cnt<lim_cnt and lim_cnt!=0:
        t_list_tmp = copy.deepcopy(t_list)
        t_list_tmp.popleft()
        op_no=op_no+1 #now the +1th annhilation operator is being seen
        while (t_list_tmp):
	    flag=1
    	    while (flag):
		flag=0
		if not t_list_tmp:
	            flag=1
		    return
		elif not t_list_tmp[0]:
		    t_list_tmp.popleft()
	            op_no=op_no+1
		    flag=1
		elif (t_list_tmp[0][0]):
		    for item in matched:
			if item.pos==t_list_tmp[0][0].pos or item.pos==full[op_no].pos:
			    flag=1
			    t_list_tmp[0].popleft()
			    break
            contracted_l.append(full[op_no])
	    contracted_r.append(t_list_tmp[0][0])
	    matched.append(full[op_no])
	    matched.append(t_list_tmp[0][0])
            fix_con(copy.copy(op_no), cnt+1, lim_cnt, copy.deepcopy(t_list_tmp), matched, contracted, contracted_l, contracted_r, a, i, u, full, f, full_pos, i_c, full_con, const_con)
	    matched.pop()
	    matched.pop()
	    t_list_tmp[0].popleft()
            if (len(t_list_tmp[0])==0):
                t_list_tmp.popleft()
		op_no=op_no+1
	    contracted_l.pop() #remove the last entered a, remove last contraction made
	    contracted_r.pop()
#-----------------------------------------------------------------------------------------------------------------------------------------
    #case when the number of contractions required are done. This we only have to print them
    elif lim_cnt!=0:
	output = deque([]) #stores the position of the output string
	#case of full contreacted terms : return by the whole function :
	full_con_term = []	
	#const_con = []
	#const_of_expression is the constant in case of a GWT
	const_of_expression = 1.0
	const_of_cumulant = 1.0	
	#lists declaration for loop factor check : spin_list_upper, spin_list_lower

	spin_list_upper=deque([])
	spin_list_lower=deque([])

	output_pos = [] #stores the actual string
	output_name = deque([]) #stores the actual string
	output_dag = deque([]) #stores the actual string
	main_list = [] #stores the main list positions
	#make the main_list positions
	if not i_c :
	    sign = 1
	else :
	    sign = -1
	new_list = []
	full_formed = [] # stores the positions of the string formed after all the contractions
	#make th main_list from full
	for item in full:
	    main_list.append(item.pos)
	#make the output list (the order of operators that are in the output formed)
	for index in range(len(contracted_l)):
	    output.append(contracted_l[index])
	    output.append(contracted_r[index])
	    #cross contraction have a 1/2 factor due to Ms summing
	    if (contracted_l[index].spin != contracted_r[index].spin and contracted_l[index].kind=='ac'):
		const_of_expression=const_of_expression*(1.0/2.0)
	    #!!!!!make the spin change of the operators here. Think
	    #print const_of_expression, contracted_l[index].spin, contracted_r[index].spin
	flag=0
	#append all the operators that are not contracted
	func.normal_order_adv(full, output)
	# make the output list in name and pos
	for item in output:
	    output_name.append(item.name)
	    output_pos.append(item.pos)
	    output_dag.append(item.dag)
	#full_formed.extend(output_pos)
	#append the contraction in the list to be printed in the tec.txt
	try:
	    for index in range(lim_cnt):
	        #When you pop an element from output, make sure is position is stored in full_formed
		tmp_1 = output.popleft()
		full_formed.append(copy.copy(tmp_1.pos))
		tmp_2 = output.popleft()
		full_formed.append(copy.copy(tmp_2.pos))
		#store spin in the list for checking the loop factor
		if tmp_1.dag=='1':
		    #print "In the spin formation dag if case: spin :", tmp_1.dag, tmp_1.spin, tmp_2.dag, tmp_2.spin
    		    spin_list_upper.append(tmp_1.pos2)
		    spin_list_lower.append(tmp_2.pos2)
		else:
		    #print "In the spin formation dag else case : spin :", tmp_1.dag, tmp_1.spin, tmp_2.dag, tmp_2.spin
		    spin_list_upper.append(tmp_2.pos2)
		    spin_list_lower.append(tmp_1.pos2)
		#print "spin list u check : it should have all contracted ", spin_list_upper, lim_cnt
		#print "spin list l check : it should have all contracted ", spin_list_lower
		

		#print "before spin change ", full_formed, full_pos, tmp_1.spin
		#change the spin of the contracted
		'''
		obj_for_spin = tmp_2.pair
		print "spin of paired ", obj_for_spin.spin, tmp_1.spin
		o = tmp_1.spin
		print o,tmp_2.spin, "loooooooook"
		tmp_2.spin = o
		obj_for_spin.spin=o
		print tmp_2.spin, tmp_1.spin
		'''

		if tmp_1.kind != 'ac':
		    tmp_3 = '\delta_{'+tmp_1.name+tmp_2.name+'}'
		    try_full_con = func.contractedobj('d', 1, 1)
		    try_full_con.upper=[tmp_1]
		    try_full_con.lower=[tmp_2]
		elif tmp_1.dag=='1':
		    tmp_3 = '\Gamma^'+tmp_1.name+'_{'+tmp_2.name+'}'
		    try_full_con = func.contractedobj('g', 1, 1)
		    #print "initiated contracted -----------", try_full_con, try_full_con.upper, '\n'
		    try_full_con.upper=[tmp_1]
		    try_full_con.lower=[tmp_2]
		elif tmp_1.dag=='0':
		    tmp_3 = '\eta^'+tmp_2.name+'_{'+tmp_1.name+'}'
		    try_full_con = func.contractedobj('e', 1, 1)
		    #print "initiated contracted -----------", try_full_con,'\n'
		    try_full_con.upper=[tmp_2]
		    try_full_con.lower=[tmp_1]
		else :
		    print "!!!!not printing anywhere, if this occurs:there may be a problem in the try contraction in fix_uv"
		new_list.append(tmp_3)

		#print "---------the try full contracted object is made ----", try_full_con.kind, try_full_con.upper, '\n'
		full_con_term.append(try_full_con)#full contracted product

		#print "to full_con_term -----------", full_con_term
	
	    #formed cumulants being appended in new_list------------------------
	    object_cumulant = []
	    #print " before object_cumulant -------- ", object_cumulant
	    const_of_cumulant, object_cumulant=func.cummulant(contracted, full_formed, new_list, spin_list_upper, spin_list_lower)

	    #print " after object_cumulant -------- ", object_cumulant
	    full_con_term.extend(object_cumulant)



	    if const_of_cumulant:
		const_of_expression = const_of_expression * const_of_cumulant
	    #const_of_expression=const_of_expression*const_from_cumulant
	# the summition thingy
	    loopcount=0.0
	    #print "loopcount ",spin_list_upper, spin_list_lower
	    loopcount = func.loop_present(spin_list_upper, spin_list_lower, -1, 0)
	    #if not output and const_of_expression!=1.0 and not cumulant_present :
	    if loopcount>0.00001:
                const_of_expression=const_of_expression*2.0*loopcount


            #print output
            if output:
                output1=returnop.returnop(full_con_term, output, new_list)
            #print output
	    #append all the normal ordered operators not contracted	
	    for item in output:
	    	full_formed.append(item.pos)


	except:
	    print "--------------------------------------------------------------------The try statement in fix_uv did not work. Something wrong in the piece of code tin 'try'"


	#print "before parity check ", full_formed, full_pos
	#parity function at work to take care of sign
        #if not output:
        #print full_formed, full_pos
	if (parity.parity(full_formed, full_pos)):
		sign=sign*(-1)
        #if not output :
        #print sign
	#make the fully contracted terms in full_con and const with sign in const_con
        ###there are terms in output which need to be made into an object and added to full_con_term

	#if output:
	#    func.write_normal_order(new_list, output)
        #print "here for check", output
        #adds uncontracted operator in new_list(printing) and full_con for later use









        ###all terms need to be added into the full_con
	#if not output :
	full_con.append(full_con_term)
	const_con.append([sign, const_of_expression])
	
	if sign == (-1):
	    tmp_5 = '$$'+"-"+str(const_of_expression)+''.join(new_list)+"\\\\"+'$$'+'\n'
	    f.write(tmp_5)
	else :
	    tmp_5 = '$$'+"+"+str(const_of_expression)+''.join(new_list)+'\\\\'+'$$'+'\n'
	    f.write(tmp_5)
#--------------------------------------------------------------------------------------------------------------------
    #The case when no contractions are made, but cummulants are there/not there
    elif lim_cnt==0:
	#In case then no further contractions are made (lim_cnt = 0) this only print operators 	
	#initialise output and others used
	output = []
	#for returning the list of fully contracted terms and constants
	full_con_term = []
	#const_con = []
	output_name = []
	const_of_expression = 1.0	
	main_list = []#used for the original string
	output_pos = []
	full_formed = [] #this stores the
	contracted_l = []#used to store the left part of a contracted string
	contracted_r = []
	new_list = []
	if not i_c: #when the string is 1st part of a commutator
	    sign = 1
	else :
	    sign = -1
	#This is where the cumulants are made through 'cumulant' function and the Latex expression is stored in new_list to be printed later
	#cumulant_present=0
	object_cumulant = []
        spin_upper = []#empty matrix required to pass into cumulant function
        spin_lower = []
	const_of_cumulant, object_cumulant=func.cummulant(contracted, full_formed, new_list, spin_upper, spin_lower)
	if const_of_cumulant:
	    const_of_expression= const_of_expression * const_of_cumulant

	#print "out of the loop for cumulant and no contraction, object_cumulant = ", object_cumulant
	#const_of_expression=const_of_expression*const_of_cumulant
	#const_of_expression=const_of_expression*const_from_cumulant
	#make the full position list - main_list
	


	for item in full:
	    main_list.append(item.pos)
	#print "out of the loop for cumulant and no contraction,  mainlist= ", main_list
	#make the normal ordered operators list in output
	

        func.normal_order(full, output, output_pos, full_formed)
	#print "out of the normal order function and no contraction, full_formed = ", full_formed, full
	if output and not new_list and i_c:
	    pass
	elif output :
	    #func.write_normal_order(new_list, output)#as the name suggest - writes the normal order in output file list
	    output=returnop.returnop(object_cumulant, output, new_list)




            #parity function at work ! Woaaa
        #print "just before parity", full_formed, full_pos
 	if (parity.parity(full_formed, full_pos)):
	    sign=sign*(-1)
	#write in list to be returned by th whole function :
	#if not output :
	full_con.append(object_cumulant)
        const_con.append([sign, const_of_expression])
	if sign == (-1):
	    tmp_5 = '$$'+"-"+str(const_of_expression)+''.join(new_list)+"\\\\"+'$$'+'\n'
	    f.write(tmp_5)
	else :
	    tmp_5 = '$$'+"+"+str(const_of_expression)+''.join(new_list)+'\\\\'+'$$'+'\n'
	    f.write(tmp_5)
