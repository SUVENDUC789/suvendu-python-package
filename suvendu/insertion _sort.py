def insertion_sort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i-1
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key

if __name__=='__main__':
    n=int(input("Enter size of list :"))
    a = []
    print("Enter list items:>")
    for i in range(n):
        item=int(input(f"Enter number [{i}] : "))
        a.append(item)

    print("Before call insertion_sort() : ",a)
    insertion_sort(a)
    print("After call insertion_sort() : ",a)
