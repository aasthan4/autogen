import copy
def swap(a,x,y):
    temp=a[x]
    a[x]=a[y]
    a[y]=temp
    return a

def permute(a, l, r, out):
    if l==r :
        out.append(copy.copy(a))
    else :
        for i in range(l,r+1):
            a=swap(a,l,i)
            #print a
            permute(a,l+1,r, out)
            a=swap(a,l,i)
#function to test the permute function. you can delete thisDDDDDDDDD
def main1():
    a=['a','b','c']
    out=[]
    permute(a,0,len(a)-1, out)
    print(out)

