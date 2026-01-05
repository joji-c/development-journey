#a function calling itself is called a recursion
#should have a base condition to stop the recursion else it will repeat until the stack is full(near a 993 times)

def say_hi(limit):
    if limit==0:
        return
    print("say hi")
    return say_hi(limit-1)

#say_hi(3)

def disp_hello_world(limit):
    if limit==0:
        return
    print("Hello World")
    return disp_hello_world(limit-1)

disp_hello_world(4)
