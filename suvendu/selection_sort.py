# selection sort

def selection_sort(a):
    for i in range(len(a)-1):
        indexOfMin = i
        j = i+1
        while j < len(a):
            if a[j] < a[indexOfMin]:
                indexOfMin = j
            j += 1

        a[indexOfMin], a[i] = a[i], a[indexOfMin]

if __name__=='__main__':
    n=int(input("Enter size of list : "))
    a=[]
    for i in range(n):
        item=int(input(f"Enter number [{i}] : "))
        a.append(item)
    print("Before call selection sort function : ",a)
    selection_sort(a)
    print("After call selection sort function : ",a)
