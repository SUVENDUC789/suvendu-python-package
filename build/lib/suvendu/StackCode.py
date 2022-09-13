# Implement stack operation (push,pop,display) using list,function (menu driven).
stack='''
def isEmpty(stack_top):
    if stack_top == -1:
        return 1
    return 0


def isFull(stack_top, stack_size):
    if stack_top == stack_size-1:
        return 1
    return 0


def Push(stack_top, stack_size, stack, value):
    if isFull(stack_top, stack_size):
        print("Stack is full ...")
    else:
        stack_top += 1
        stack.append(value)
    return stack_top


def Pop(stack_top, stack):
    if isEmpty(stack_top):
        print("Stack is empty ...")
    else:
        value = stack[stack_top]
        print("Deleted element is : ", value)
        del stack[stack_top]
        stack_top -= 1
    return stack_top


def display(stack_top, stack):
    if isEmpty(stack_top):
        print("Stack is empty ! ...")
    else:
        print("Stack element are :> ")
        size = len(stack)-1
        while size >= 0:
            print(stack[size])
            size -= 1


if __name__ == '__main__':
    stack_top = -1
    stack_size = int(input("Enter stack size : "))
    stack = []
    ch = {'1': 'Push', '2': 'Pop', '3': 'Display', '4': 'quit'}
    while True:
        print(ch)
        choice = input("Enter your choice : ")
        if ch.get(choice) == 'Push':
            value = input("Enter value : ")
            stack_top = Push(stack_top, stack_size, stack, value)
        elif ch.get(choice) == 'Pop':
            stack_top = Pop(stack_top, stack)
        elif ch.get(choice) == 'Display':
            display(stack_top, stack)
        elif ch.get(choice) == 'quit':
            print("Thank you ?")
            exit()
        else:
            print("Please enter correct choice !...")
            
'''
