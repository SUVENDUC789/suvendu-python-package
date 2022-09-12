# Create a calculator using switch function such the press 1 for addition,2 for subtraction ,3 for multiplication,4 for division .

def switchFun(choicedict,a,b,ch):
    val=choicedict.get(ch)
    if val == "Addition":
        return a+b
    elif val == "Substraction":
        return a-b      
    elif val == "Multiplication":
        return a*b      
    elif val == "Division":
        return a/b 
    else :
        return "Invalid choice"


a=eval(input("Enter first number : "))
b=eval(input("Enter second number : "))
choice={1:"Addition",2:"Substraction",3:"Multiplication",4:"Division"}
ch=input(f"Enter your choice : {choice} :>")
try:
    ch=int(ch)
    c=switchFun(choice,a,b,ch)
    print(f"Result is : {c}")
except:
    print("Some thing went to wrong ...")