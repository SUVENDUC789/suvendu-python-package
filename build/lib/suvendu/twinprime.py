# Find twin-prime within a given range.

def twinPrimeWithinaGivenRange(startingnumber,lastnumber):
    def Prime(num):
        flag=0
        for i in range(2,num):
            if num%i == 0:
                flag=1
                break
        
        if flag == 0 :
            return 1
        else :
            return 0

    print(f"Prime number in range {startingnumber} <= {lastnumber} :>")
    for i in range(startingnumber,lastnumber+1):
        if Prime(i)==1 :
            print(i,end="   ")