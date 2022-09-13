# year = int(input("Enter year : "))

def isLeapYear(year):
    if (year % 100 == 0 ) :
        print(f"{year} is not leap year ")
    elif (year % 400 == 0): 
        print(f"{year} is leap year ")
    elif(year % 4 == 0):
        print(f"{year} is leap year ")
    else:
        print(f"{year} is not leap year ")
