from . import class_term
from pkg import parity
def eq(a,b,t1,t2):
    if a in t1.sum_list and b in t2.sum_list:
        if t1.isi(a) and t2.isi(b):
            return 1
        elif t1.isa(a) and t2.isa(b):
            return 1
    else :
        return 0

def eq8(list1,list2,t1,t2):
    tmp_order1=[]
    print(list1, list2, t1.sum_list, t2.sum_list)
    for i11 in list1:
        found=0
        for i22 in list2:
            if i11==i22:
                tmp_order1.append(list2.index(i22))
                found=1

        if found==0 and list1.index(i11)<len(list1)/2:
            for i22 in range(len(list2)/2):
                if eq(i11, list2[i22], t1,t2):
                    tmp_order1.append(i22)
                    found=1
        if found==0 and list1.index(i11)>=len(list1)/2:
            for i22 in range(len(list2)/2,len(list1)):
                if eq(i11, list2[i22], t1,t2):
                    tmp_order1.append(i22)
                    found=1
        if found==0:
            print("not same")
            return 0.0
    if len(tmp_order1)==2:
        tmp1= parity.parity([0,1],tmp_order1)
        print(tmp1)
    else:
        tmp1= parity.parity([0,1,2,3],tmp_order1)
        print(tmp1)
    if tmp1%2==0:
        return 1.0
    elif tmp1%2==1:
        return -1.0
def eq821(list1, list2, t1, t2):

    if list1[2]==list2[0] or eq(list1[2],list2[0],t1,t2):
        if list1[3]==list2[1] or eq(list1[3],list2[1],t1,t2):
            if list1[0]==list2[2] or eq(list1[0],list2[2],t1,t2):
                if list1[1]==list2[3] or eq(list1[1],list2[3],t1,t2):

                    print("case1")
                    return 1.0
            elif list1[1]==list2[2] or eq(list1[1],list2[2],t1,t2):
                if list1[0]==list2[3] or eq(list1[0],list2[3],t1,t2):
                    print("case1")
                    return -1.0
    elif list1[3]==list2[0] or eq(list1[3],list2[0],t1,t2):
        if list1[2]==list2[1] or eq(list1[2],list2[1],t1,t2):
            if list1[0]==list2[2] or eq(list1[0],list2[2],t1,t2):
                if list1[1]==list2[3] or eq(list1[1],list2[3],t1,t2):
                    print("case2")
                    return -1.0
            elif list1[1]==list2[2] or eq(list1[1],list2[2],t1,t2):
                if list1[0]==list2[3] or eq(list1[0],list2[3],t1,t2):
                    print("case2")
                    return 1.0

    elif list1[1]==list2[0] or eq(list1[1],list2[0],t1,t2):
        print(t1.sum_list, t2.sum_list, list1[1],list2[0])
        if list1[0]==list2[1] or eq(list1[0],list2[1],t1,t2):
            if list1[2]==list2[2] or eq(list1[2],list2[2],t1,t2):
                if list1[3]==list2[3] or eq(list1[3],list2[3],t1,t2):
                    print("case31")
                    return -1.0
            elif list1[3]==list2[2] or eq(list1[3],list2[2],t1,t2):
                if list1[2]==list2[3] or eq(list1[2],list2[3],t1,t2):
                    print("case32")
                    return 1.0
    elif list1[0]==list2[0] or eq(list1[0],list2[0],t1,t2):
        if list1[1]==list2[1] or eq(list1[1],list2[1],t1,t2):
            if list1[2]==list2[2] or eq(list1[2],list2[2],t1,t2):
                if list1[3]==list2[3] or eq(list1[3],list2[3],t1,t2):
                    print("case4")
                    return 1.0
            elif list1[3]==list2[2] or eq(list1[3],list2[2],t1,t2):
                if list1[2]==list2[3] or eq(list1[2],list2[3],t1,t2):
                    print("case4")
                    return -1.0

    return 0.0
def eq81(list1, list2, t1, t2):
    if list1[0]==list2[0] or eq(list1[0],list2[0],t1,t2):
        if list1[1]==list2[1] or eq(list1[1],list2[1],t1,t2):
            return 1.0
    elif list1[0]==list2[1] or eq(list1[0],list2[1],t1,t2):
        if list1[1]==list2[0] or eq(list1[1],list2[0],t1,t2):
            return -1.0
    return 0.0
