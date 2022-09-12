# Merge two list into one list in such a manner that  new list contain 1st data from 1st list 2nd data from 2nd list again 3rd data from 1st list and 4th data from 2nd list.(note. Input two list may or may not be of same length).

def createList(a,n):
    for i in range(n):
        item=input("Enter Value : ")
        a.append(item)

def Merge(a,b):
    c=[]
    if len(a) == len(b):
        for i in range(len(a)):
            c.append(a[i])
            c.append(b[i])

    elif len(a)>len(b):
        start=0
        stop=len(b)-1
        while start<=stop:
            c.append(a[start])
            c.append(b[start])
            start+=1
        start=len(b)
        stop=len(a)
        while start<stop:
            c.append(a[start])
            start+=1
    elif len(a)<len(b):
        start=0
        stop=len(a)-1
        while start<=stop:
            c.append(a[start])
            c.append(b[start])
            start+=1
        start=len(a)
        stop=len(b)
        while start<stop :
            c.append(b[start])
            start+=1


    print(c)

na=int(input("Enter size of first list : "))
a=[]
createList(a,na)

nb=int(input("Enter size of first list : "))
b=[]
createList(b,nb)
print("Array element are : ",a)
print("Array element are : ",b)
print("After merge two list :>")
Merge(a,b)
