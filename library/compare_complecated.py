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
    for c1 in coeff:
        for j in c1:
            if j.seen==0 and j.name==i.name:
                flag2=1
                return j
    if flag2==0:
        return NULL
def coeff_seen(coeff):
    flag2=1
    for c1 in coeff:
        for i in c2:
            if i.seen==0:
                flag2=0
    return flag2
def swap(c1):
    tmp = c1[2]
    c[2]=c[3]
    c[3]=tmp


def pick(coeff1, coeff2):
    for c1 in reversed(range(len(coeff1))):
        if len(coeff1[c1])==2 and coeff1[c1,1].seen==0:
            return c1,coeff1[c1,1], coeff2[c1,1]
        elif len(coeff1[c1])==4:

            if coeff1[c1,2].seen==0:
                return c1,coeff1[c1,2], coeff2[c1,2]
            elif coeff1[c1,3].seen==0:
                return c1,coeff1[c1,3], coeff2[c1,3]
    print "something is wrong in picking"
    exit()


def level1(term1,term2):
    #Level 1 : same operators (redundant )
    if len(term1.map_org)!=len(term2.map_org):
        return 0
    for item1 in term1.map_org:
        flag1=0
        for item2 in term2.map_org:
            if item1==item2:
                flag1=1
        if flag1!=1:
            return 0
    return 1

def level2(term1,term2):
    #position of non dummy indeces is the same, if not, exchange
    for ind in range(len(term1.coeff_list)):
        flag1 =1
        for item in term1.coeff_list[ind]:
            if not term1.is_dummy(item):
                if item not in term2.coeff_list[ind]:
                    flag1=0
                if flag1 ==0:
                    for c in range(len(term2.coeff_list)):
                        if item in term2.coeff_list[c]:
                            #swap c and ind in term2 if they are of same type (also swap stuff in map_org

                            tmp=term2.coeff_list[ind]
                            term2.coeff_list[ind]=term2.coeff_list[c]
                            term2.coeff_list[c]=tmp

                            tmp=term2.map_org[ind]
                            term2.map_org[ind]=term2.map_org[c]
                            term2.map_org[c]=tmp

                            flag1 =1
                    if flag1==0:
                        return 0

def level3(term1,term2):
    #type and count of dummy of each type is the same in each coeff
    for c1,c2 in zip(term1.coeff_list,term2.coeff_list):
        if len(c1)==len(c2):
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
            if a1!=a2 or ii1!=ii2:
                return 0
        else:
            return 0

def level4(term1, term2):
    #build class objects, find pair and follow pair till everything is seen
    #build objects
    tmp1=[]
    tmp2=[]

    for c1 in range(len(term1.coeff_list)):
        for i1 in term1.coeff_list[c1]:
            print c1, term1.map_org[c1]
            x1=ind(i1,0,term1.map_org[c1])
            tmp1.append(x1)
        tmp2.append(tmp1)
    coeff1=tmp2
    for c2 in range(len(term2.coeff_list)):
        for i2 in term2.coeff_list[c2]:
            print c2, term2.map_org[c2]
            x2=ind(i2,0,term2.map_org[c1])
            tmp1.append(x2)
        tmp2.append(tmp1)
    coeff2=tmp2
    #pair the pairs

    for c1 in coeff1:
        if len(c1)==2:
            c1[0].pair=c1[1]
            c1[1].pair=c1[0]
        elif len(c1)==4:
            c1[0].pair=c[2]
            c1[1].pair=c[3]
            c1[2].pair=c[0]
            c1[3].pair=c[1]
    for c1 in coeff2:
        if len(c1)==2:
            c1[0].pair=c1[1]
            c1[1].pair=c1[0]
        elif len(c1)==4:
            c1[0].pair=c[2]
            c1[1].pair=c[3]
            c1[2].pair=c[0]
            c1[3].pair=c[1]
    while coeff_seen(coeff1):
        if flag1==0:
            #pick item from the end
            c1,i1, i2 =pick(coeff1, coeff2)

        else :
            i1=find_ind(coeff1,i1)
            i2=find_ind(coeff2,i2)
            also pick the coeff number
            i1.seen=1
            i2.seen=1
        else:
        #go to its pair and check on the other term too
        i1,i2=i1.pair,i2.pair
        i1.seen=1
        i2.seen=1
        matched=0
        if term1.type(i1)==term2.type(i2):
            if not term1.is_dummy(i1) and not term2.is_dummy(i2) and i1.name==i2.name:
                they are same move forward
                i1=i1.pair# - dont pair up just yet

                i2=i2.pair
                matched=1
            elif term1.is_dummy(i1) and term2.is_dummy(i2):
                matched=1
        if matched==0 :
            you have the coeff number
            #try switching and send again
            swap(coeff
        else :
            #find i1,i2 in another coeff
            if find_ind(coeff1,i1)==NULL:
                flag1==0
            elif find_ind(coeff1,i1)!=find_ind(coeff2,i2):
                #switch the i's in the old coeff number and check again
                flag1==1

        #if match for ij not found, use another pick else us the same
        #if not match swap and check, if match good else return no
        #if all are seen good else repeat

def compare(term1, term2):
    flag=1

    if flag==1:
        flag=level1(term1,term2)
    if flag!=0:
        flag=level2(term1,term2)
    if flag!=0:
        flag=level3(term1,term2)
    if flag!=0:
        flag=level4(term1,term2)
    #if flag!=0:
        #flag=level1(term1,temr2)

    return flag

