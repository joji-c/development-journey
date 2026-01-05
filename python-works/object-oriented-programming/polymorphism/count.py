class NumberCount:
    def solution(*args,**kwargs):
        count=0
        op=int(kwargs.get("value"))
        for i in args:
            if i == op:
                count+=1
        print(count)

num=NumberCount()
num.solution(10,10,20,30,10,10,40,50,value=10)

"""
OR

num_list=list(args)
val=int(kwargs.get("value))
return num_list.count(val)
"""
