import parity
import copy
def create_map(term,coeff,ind):
    map_out=[]
            for c in coeff:
                found=0
                for i in range(len(term.coeff_list)):
                    for j in range(len(term.coeff_list[i])):
                        if term.coeff_list[i][j]==c and i!=ind:
                            map_out.append(term.large_op_list[i].name)
                            found=1
                            print 'contraction found'
                            break
                if found==0:
                    print 'open index'
                    map_out.append(term.large_op_list[ind].name)
    return map_out
#produces all possible permutations of a 4,6,8 index coeff/operator for comparing
# with correct sign
#Algo : simple 1. produce all permutations through functions.permutations
#--------then use the parity.paritty to decide sign and add all up in a list
#--------send it to the levels for comparision.
def sign_coeff(term1,term2,pos):
    c=term2.coeff_list[pos]
    possible_coeff_tmp=[]
    possible_coeff=[]
    if len(c)==4:
        possible_coeff=[[c[0],c[1],c[3],c[2]],[c[1],c[0],c[3],c[2]],[c[1],c[0],c[2],c[3]],[c[0],c[1],c[2],c[3]]]
    #map_op=create_map(term2,coeff,pos)
    #create all possibilities of terms using permute function
    #elif len(c)==6:
    #	functions.permute(c,3,5,possible_coeff_tmp)
    #	for item in possible_coeff_tmp:
    #	    functions.permute(item,3,5, possible_coeff)
    #print 'test that all permutations are created of operators',possible_coeff
    #sys.exit(0)
    for coeff in possible_coeff:
        map_op=create_map(term2,coeff,pos)

    #create the sign of each term using parity function
    for c1 in possible_coeff:
        tmp_term.coeff_list[pos]=c1
	if parity.parity(c1,term.coeff_list[pos])==1:
	    tmp_term.fac=term.fac*-1
	else :
	    tmp_term.fac=term.fac
	#print 'check the sign of terms in juggle', c1,term.coeff_list[pos], parity.parity(c1,term.coeff_list[pos]),"(",tmp_term.fac,term.fac,")"

        ret_terms.append(copy.deepcopy(tmp_term))
    #print ' length og list terms after juggle is :', len(ret_terms)

    return ret_terms
def level3_sign(term1,term2):
    print 'into sign function'
    return 1
