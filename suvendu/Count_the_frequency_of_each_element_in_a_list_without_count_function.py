# Count the frequency of each element in a list(arrary).without count function.
def list_element_count(a,num):
    count=0
    for i in a :
        if num == i :
            count=count+1
    return count

n=int(input("enter list size :"))   
a=[]
for i in range(n):
    num=int(input(f"Enter number [{i}]"))
    a.append(num)
b=set(a)
print("List elemnt are : ",a)
for i in b:
    print(f"List element are : {i} | frequency is : {list_element_count(a,i)}")