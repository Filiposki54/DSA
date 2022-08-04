#Create  stack
def create_stack():
    stack = []
    return stack


#Check an empty stack
def check_empty(stack):
    return len(stack) == 0


#Adding items into the stack
def push(stack, item):
    stack.append(item)
    print("pushed item: " + item)


#Removing items from the stack
def pop(stack):
    if (check_empty(stack)):
        return "stack is empty"

    return stack.pop()


stack = create_stack()
push(stack, "Bob")
push(stack, str(100))
push(stack, "James")
print("popped item: " + pop(stack))
print("stack after popping an element" + str(stack))