#IMPLEMENT STACK USING LIST
stack=[]
max=7
top=-1

def push(stack):
    global top
    if top == max - 1:
        print("Stack Overflow! Cannot push\n");
    else:
        value=int(input("Enter value to push: "))
        top=top+1
        stack.append(value)
        print(value,"pushed to stack\n")
    

def pop(stack):
    global top
    if top == -1:
        print("Stack Underflow! Cannot pop\n")
    else:
        num = stack.pop()
        print("Popped value:", num)
        top-=1


def peek(stack):
    if top == -1:
        print("Stack is empty! No top element\n")
    else:
        print("Top value: ", stack[top])
    

def show(stack):
    if top == -1:
        print("Stack is empty!\n")
    else:
        print("Stack elements: ")
        for i in range (len(stack)):
            print(stack[i])
    

while (1):
        print("\nStack Operations:\n")
        print("1. Push\n2. Pop\n3. Peek\n4. Display\n")
        ch=int(input("Enter your choice: "))
        if ch==1:
            push(stack)
        elif ch==2:
            pop(stack)
        elif ch==3:
            peek(stack)
        elif ch==4:
            show(stack)
        else:
            print("Invalid Input")

