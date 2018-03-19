import copy
a=[1,2,3]

def swap (a, b,c):
    tmp = a[c]
    a[c]=a[b]
    a[b]=tmp
ret=[]
def heapit(a, size, n):
    global ret
    if size ==1:
        ret.append(copy.deepcopy(a))
        return 
    for i in range(size):
        heapit(a, size-1, n)
        if (size%2)==1:
            swap(a,0, size-1)
        else : 
            swap(a,i, size-1)
    return ret
print heapit(a, 3, 3)
