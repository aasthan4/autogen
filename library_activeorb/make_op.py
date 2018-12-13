#Development : adding operators Tiu,Tua,T(ij->ua),T(ij->uv),T(uv->ab),T(ui->va),T(ui->ab),T(uv->wx)
#Think about how F and V functions will be edited to incorporate active orbitals. 
#Progress : added nextop,and t1i->u.
#TO DO next: change operator naming system from T1 to Z1i->u and add others. 
from pkg import func_ewt 
import class_large_operator as class1
from next_op import next_op
def count_list(dict_ind):
    a=0
    p=0
    i=0
    u=0
    for key, value in dict_ind.items():

	if key>='a' and key<='h':
	    a=a+1
	elif key>='p' and key<='t':
	    p=p+1
	elif key>='i' and key<='n':
	    i=i+1
        elif key>='u' and key<='z':
            u=u+1
	elif len(key)==2:
	    if key[0]>='a' and key[0]<='h':
	        a=a+1
	    elif key[0]>='p' and key[0]<='t':
	        p=p+1
	    elif key[0]>='i' and key[0]<='n':
	        i=i+1
	    elif key[0]>='u' and key[0]<='z':
	        u=u+1
	
    return [i,a,p,u]
def make_op(list_op, dict_ind):
    #dict_ind={}
    list_main=[]
    list_type=count_list(dict_ind)
    #list_type=[0,0,0]
    for lop in list_op:
	#deactivate U operators
        if lop[0]=='F':
            fac=1.0
            summ=[next_op('p',list_type,0),next_op('p',list_type,1)]
            coeff=[next_op('p',list_type,0),next_op('p',list_type,1)]
            opp=func_ewt.contractedobj('op', 1, 1)
            opp.upper=[next_op('p',list_type,0)]

            opp.lower=[next_op('p',list_type,1)]

            dict_ind[next_op('p',list_type,0)]=lop
            dict_ind[next_op('p',list_type,1)]=lop
            stp=[[opp]]
            co=[[1,1]]

            F = class1.large_operator(lop,fac, summ, coeff, stp, co)



            list_main.append(F)
            list_type[2]+=2

	    print summ,opp.upper,opp.lower
        elif lop[0]=='V':
            fac=1.0/4.0
            #num=ord('p')+list_type[2]

            summ=[next_op('p',list_type,0),next_op('p',list_type,1),next_op('p',list_type,2),next_op('p',list_type,3)]
            coeff=[next_op('p',list_type,0),next_op('p',list_type,1),next_op('p',list_type,2),next_op('p',list_type,3)]
            opp=func_ewt.contractedobj('op', 1, 1)
            opp.upper=[next_op('p',list_type,0),next_op('p',list_type,1)]
            print '!!!!!!!!---------',opp.upper
            opp.lower=[next_op('p',list_type,2),next_op('p',list_type,3)]
            print opp.lower
            dict_ind[next_op('p',list_type,0)]=lop
            dict_ind[next_op('p',list_type,1)]=lop
            dict_ind[next_op('p',list_type,2)]=lop
            dict_ind[next_op('p',list_type,3)]=lop
            stp=[[opp]]
            co=[[1,1]]

            V = class1.large_operator(lop,fac, summ, coeff, stp, co)

            list_main.append(V)
            list_type[2]+=4

	    print summ,opp.upper,opp.lower
        elif lop[0]=='D' and lop[1]=='1':



            #num1=ord('i')+list_type[0]
            #num2=ord('a')+list_type[1]
            #summ=[chr(num1), chr(num2)]
	    #summ=[]
            fac=1.0
            #coeff=[]
            summ=[next_op('i',list_type,0),next_op('a',list_type,0)]
            coeff=[next_op('i',list_type,0),next_op('a',list_type,0)]
            opp=func_ewt.contractedobj('op', 1, 1)
            opp.upper=[next_op('i',list_type,0)]
            opp.lower=[next_op('a',list_type,0)]
            st=[[opp]]
            co=[[1,1]]
            dict_ind[next_op('i',list_type,0)]=lop
            dict_ind[next_op('a',list_type,0)]=lop

            X1 = class1.large_operator(lop,fac, summ, coeff, st, co)
            list_main.append(X1)

            list_type[0]+=1
            list_type[1]+=1
	    print summ,opp.upper,opp.lower
        elif lop[0]=='X' and lop[1]=='1':
            #num1=ord('i')+list_type[0]
            #num2=ord('a')+list_type[1]
            fac=1.0
            #summ=['i','j','a','b']
            summ=[]
            #coeff=['i','j','a','b']
            coeff=[]
            opp=func_ewt.contractedobj('op', 1, 1)
            opp.upper=[next_op('i',list_type,0)]
            opp.lower=[next_op('a',list_type,0)]
            st=[[opp]]
            co=[[1,1]]
            dict_ind[next_op('i',list_type,0)]=lop
            dict_ind[next_op('a',list_type,0)]=lop
            X1 = class1.large_operator(lop,fac, summ, coeff, st, co)
            list_main.append(X1)

            list_type[0]+=1
            list_type[1]+=1



	    print summ,opp.upper,opp.lower
        elif lop[0]=='D' and lop[1]=='2':
            fac=1.0/4.0
            #num1=ord('i')+list_type[0]
            #num2=ord('a')+list_type[1]
            #summ=['i','j','a','b']
            #summ=[chr(num1), ]
            #coeff=['i','j','a','b']
            #coeff=[]

            summ=[next_op('i',list_type,0),next_op('i',list_type,1),next_op('a',list_type,0),next_op('a',list_type,1)]
            coeff=[next_op('i',list_type,0),next_op('i',list_type,1),next_op('a',list_type,0),next_op('a',list_type,1)]
            opp=func_ewt.contractedobj('op', 1, 1)
            opp.upper=[next_op('i',list_type,0),next_op('i',list_type,1)]
            opp.lower=[next_op('a',list_type,0),next_op('a',list_type,1)]
            st=[[opp]]
            co=[[1,1]]
            dict_ind[next_op('i',list_type,0)]=lop
            dict_ind[next_op('i',list_type,1)]=lop
            dict_ind[next_op('a',list_type,0)]=lop
            dict_ind[next_op('a',list_type,1)]=lop

            X2 = class1.large_operator(lop,fac, summ, coeff, st, co)
            list_main.append(X2)


            list_type[0]+=2
            list_type[1]+=2

	    print summ,opp.upper,opp.lower
        elif lop[0]=='Y' and lop[1]=='2':
            fac=1.0
            #num1=ord('a')+list_type[1]
            #num2=ord('i')+list_type[0]
            #summ=['i','j','a','b']
            summ=[]
            #coeff=['i','j','a','b']
            coeff=[]
            opp=func_ewt.contractedobj('op', 1, 1)
            opp.upper=[chr(num1),chr(num1+1)]
            opp.lower=[chr(num2),chr(num2+1)]
            st=[[opp]]
            co=[[1,1]]
            dict_ind[chr(num1)]=lop
            dict_ind[chr(num1+1)]=lop
            dict_ind[chr(num2)]=lop
            dict_ind[chr(num2+1)]=lop

            X2 = class1.large_operator(lop,fac, summ, coeff, st, co)
            list_main.append(X2)


            list_type[0]+=2
            list_type[1]+=2


        elif lop[0]=='X' and lop[1]=='2':
            fac=1.0
            #num1=ord('i')+list_type[0]
            #num2=ord('a')+list_type[1]
            #summ=['i','j','a','b']
            summ=[]
            #coeff=['i','j','a','b']
            coeff=[]
            opp=func_ewt.contractedobj('op', 1, 1)
            opp.upper=[next_op('i',list_type,0),next_op('i',list_type,1)]
            opp.lower=[next_op('a',list_type,0),next_op('a',list_type,1)]
            st=[[opp]]
            co=[[1,1]]
            dict_ind[next_op('i',list_type,0)]=lop
            dict_ind[next_op('i',list_type,1)]=lop
            dict_ind[next_op('a',list_type,0)]=lop
            dict_ind[next_op('a',list_type,1)]=lop

            X2 = class1.large_operator(lop,fac, summ, coeff, st, co)
            list_main.append(X2)


            list_type[0]+=2
            list_type[1]+=2

	    print summ,opp.upper,opp.lower


        elif lop[0]=='T' and lop[1]=='1':
            #num1=ord('i')+list_type[0]
            #num2=ord('a')+list_type[1]
            fac=1.0
            summ=[next_op('a',list_type,0),next_op('i',list_type,0)]
            coeff=[next_op('a',list_type,0),next_op('i',list_type,0)]
            #coeff=[chr(num2),chr(num1)]
            opp=func_ewt.contractedobj('op', 1, 1)
            opp.upper=[next_op('a',list_type,0)]
            opp.lower=[next_op('i',list_type,0)]
            stt=[[opp]]
            co=[[1,1]]
            dict_ind[next_op('a',list_type,0)]=lop
            dict_ind[next_op('i',list_type,0)]=lop
            T1 = class1.large_operator(lop,fac, summ, coeff, stt, co)
            list_main.append(T1)
            list_type[0]+=1
            list_type[1]+=1
	    print summ,opp.upper,opp.lower
        elif lop[0]=='Z' and lop[1]=='1':
            #num1=ord('i')+list_type[0]
            #num2=ord('a')+list_type[1]
            fac=1.0
            summ=[next_op('u',list_type,0),next_op('i',list_type,0)]
            coeff=[next_op('u',list_type,0),next_op('i',list_type,0)]
            #coeff=[chr(num2),chr(num1)]
            opp=func_ewt.contractedobj('op', 1, 1)
            opp.upper=[next_op('u',list_type,0)]
            opp.lower=[next_op('i',list_type,0)]
            stt=[[opp]]
            co=[[1,1]]
            dict_ind[next_op('u',list_type,0)]=lop
            dict_ind[next_op('i',list_type,0)]=lop
            T1 = class1.large_operator(lop,fac, summ, coeff, stt, co)
            list_main.append(T1)
            list_type[0]+=1
            list_type[1]+=1
	    print summ,opp.upper,opp.lower
        elif lop[0]=='T' and lop[1]=='2':

            #num1=ord('i')+list_type[0]
            #num2=ord('a')+list_type[1]
            fac=1.0/4.0


            summ=[next_op('a',list_type,0),next_op('a',list_type,1),next_op('i',list_type,0),next_op('i',list_type,1)]
            coeff=[next_op('a',list_type,0),next_op('a',list_type,1),next_op('i',list_type,0),next_op('i',list_type,1)]
            #coeff=[chr(num2),chr(num2+1),chr(num1),chr(num1+1)]
            opp=func_ewt.contractedobj('op', 1, 1)
            opp.upper=[next_op('a',list_type,0),next_op('a',list_type,1)]
            opp.lower=[next_op('i',list_type,0),next_op('i',list_type,1)]
            stt=[[opp]]
            co=[[1,1]]

            dict_ind[next_op('a',list_type,0)]=lop
            dict_ind[next_op('a',list_type,1)]=lop
            dict_ind[next_op('i',list_type,0)]=lop
            dict_ind[next_op('i',list_type,1)]=lop
            list_type[0]+=2
            list_type[1]+=2


            T2 = class1.large_operator(lop,fac, summ, coeff, stt, co)
            list_main.append(T2)
	    print summ,opp.upper,opp.lower
        else :
            print "input error in making operators--------------------"
    return list_main, dict_ind
