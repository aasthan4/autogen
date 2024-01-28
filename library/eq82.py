from . import class_term
def eq(a,b,t1,t2):
    if a in t1.sum_list and b in t2.sum_list:
        if t1.isi(a) and t2.isi(b):
            return 1
        elif t1.isa(a) and t2.isa(b):
            return 1
    else :
        return 0

def eq82(list1, list2, t1, t2):

    flag =0

    if list1[2]==list2[0]:
        if list1[3]==list2[1] :
            if list1[0]==list2[2] :
                if list1[1]==list2[3] :
                    flag=1
                    return 1.0
            elif list1[1]==list2[2] :
                if list1[0]==list2[3]:
                    flag=-1
                    return -1.0
    elif list1[3]==list2[0] :
        if list1[2]==list2[1] :
            if list1[0]==list2[2] :
                if list1[1]==list2[3] :
                    flag=-1
                    return -1.0
            elif list1[1]==list2[2] :
                if list1[0]==list2[3] :
                    flag=1
                    return 1.0
    elif list1[0]==list2[0] :
        if list1[1]==list2[1] :
            if list1[2]==list2[2] :
                if list1[3]==list2[3]:
                    flag=1
                    return 1.0
            elif list1[3]==list2[2] :
                if list1[2]==list2[3] :
                    flag=-1
                    return -1.0
    elif list1[1]==list2[0] :
        if list1[0]==list2[1] :
            if list1[2]==list2[2] :
                if list1[3]==list2[3] :
                    flag=-1
                    return -1.0
            elif list1[3]==list2[2] :
                if list1[2]==list2[3] :
                    flag=1
                    return 1.0


    if list1[2]==list2[0] or eq(list1[2],list2[0],t1,t2):
        if list1[3]==list2[1] or eq(list1[3],list2[1],t1,t2):
            if list1[0]==list2[2] or eq(list1[0],list2[2],t1,t2):
                if list1[1]==list2[3] or eq(list1[1],list2[3],t1,t2):
                    return 1.0
            elif list1[1]==list2[2] or eq(list1[1],list2[2],t1,t2):
                if list1[0]==list2[3] or eq(list1[0],list2[3],t1,t2):
                    return -1.0
    elif list1[3]==list2[0] or eq(list1[3],list2[0],t1,t2):
        if list1[2]==list2[1] or eq(list1[2],list2[1],t1,t2):
            if list1[0]==list2[2] or eq(list1[0],list2[2],t1,t2):
                if list1[1]==list2[3] or eq(list1[1],list2[3],t1,t2):
                    return -1.0
            elif list1[1]==list2[2] or eq(list1[1],list2[2],t1,t2):
                if list1[0]==list2[3] or eq(list1[0],list2[3],t1,t2):
                    return 1.0
    elif list1[0]==list2[0] or eq(list1[0],list2[0],t1,t2):
        if list1[1]==list2[1] or eq(list1[1],list2[1],t1,t2):
            if list1[2]==list2[2] or eq(list1[2],list2[2],t1,t2):
                if list1[3]==list2[3] or eq(list1[3],list2[3],t1,t2):
                    return 1.0
            elif list1[3]==list2[2] or eq(list1[3],list2[2],t1,t2):
                if list1[2]==list2[3] or eq(list1[2],list2[3],t1,t2):
                    return -1.0
    elif list1[1]==list2[0] or eq(list1[1],list2[0],t1,t2):
        if list1[0]==list2[1] or eq(list1[0],list2[1],t1,t2):
            if list1[2]==list2[2] or eq(list1[2],list2[2],t1,t2):
                if list1[3]==list2[3] or eq(list1[3],list2[3],t1,t2):
                    return -1.0
            elif list1[3]==list2[2] or eq(list1[3],list2[2],t1,t2):
                if list1[2]==list2[3] or eq(list1[2],list2[3],t1,t2):
                    return 1.0

    return 0.0
def eq81(list1, list2, t1, t2):
    if list1[0]==list2[0] or eq(list1[0],list2[0],t1,t2):
        if list1[1]==list2[1] or eq(list1[1],list2[1],t1,t2):
            return 1.0
    elif list1[0]==list2[1] or eq(list1[0],list2[1],t1,t2):
        if list1[1]==list2[0] or eq(list1[1],list2[0],t1,t2):
            return -1.0
    return 0.0
