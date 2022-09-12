def binarySearch(a,low,high,search):
    try:
        if low <= high :
            mid=int((low+high)/2)
            if a[mid] == search :
                return mid
            elif a[mid] > search :
                return binarySearch(a,low,mid-1,search)
            else:
                return binarySearch(a,mid+1,high,search)
    except:
            return -108

n=int(input("Enter size of list : "))
a=[]
for i in range(n):
    value=int(input(f"Enter number [{i}]"))
    a.append(value)

# a=[10,20,30,40,50,60,70,80,90]
search=int(input("Enter search element : "))

if binarySearch(a,0,len(a),search) == -108 :
    print(f"{search} element not found !")
else :
    print(f"{search} element found at {binarySearch(a,0,len(a),search)}")

print("List elemnt are : ",a)