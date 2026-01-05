def add(*args):
    print(sum(args))

add(10,20)
add(10,20,30)
add(10,20,30,40)

print()

def display(**kwargs):
        print(kwargs)

display(name="joji",age=22,place="thrissur")

print()

def operations(*args,**kwargs):
    op=kwargs.get("key")
    if op=="max":
         print("largest num:",max(args))
    elif op=="min":
         print("smallest num:",min(args))

operations(10,20,30,40,key="max")
operations(10,20,30,40,key="min")

