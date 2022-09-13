# Find prime factor of a number.
def PrimeFactor(n):
    def rangeBasedPrime(rangeofnumber):
        a = []
        for i in range(rangeofnumber+1):
            flag = 0
            if i == 0 or i == 1:
                flag = 1
            for j in range(2, (int(i/2)+1)):
                if i % j == 0:
                    flag = 1
                    break
            if flag == 0:
                a.append(i)
        return a

    a = rangeBasedPrime(10000)
    b = []
    while n != 1:
        for i in range(len(a)):
            if n % a[i] == 0 and n > a[i]:
                n = n//a[i]
                # print(n, a[i])
                b.append(a[i])

            elif n == a[i]:
                n = n//a[i]
                # print(n, a[i])
                b.append(a[i])
                break

    p = 1
    for i in range(len(b)):
        p = p*b[i]
    print(p," prime factor = ",b)
