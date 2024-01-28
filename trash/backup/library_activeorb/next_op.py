#gap=0 in case you want nextt and +1 if you want next to next etc
def next_op(type_ind,type_list,gap):

    if type_ind=='u':
	char=chr(ord('u')+(type_list[2]+gap)%5)
	no=(type_list[3]+gap)//5
	#'''
	if no==0:
	    return char
	else:
	#'''
	    return ''.join([char,str(no)])
    if type_ind=='p':
	char=chr(ord('p')+(type_list[2]+gap)%5)
	no=(type_list[2]+gap)//5
	#'''
	if no==0:
	    return char
	else:
	#'''
	    return ''.join([char,str(no)])
    if type_ind=='a':
	char=chr(ord('a')+(type_list[1]+gap)%8)
	no=(type_list[1]+gap)//8
	#'''
	if no==0:
	    return char
	else:
	#'''
	    return ''.join([char,str(no)])
    if type_ind=='i':
	char=chr(ord('i')+(type_list[0]+gap)%6)
	no=(type_list[0]+gap)//6
	#'''
	if no==0:
	    return char
	else:
	#'''
	    return ''.join([char,str(no)])
