class IsFibonacci:
    def solution(self,number):
        is_fibo_num=False
        p=0
        c=1
        fibo=[]
        fibo.append(p)
        fibo.append(c)
        n=p+c
        while n<=number:
            n=p+c
            fibo.append(n)
            p=c
            c=n
        for f in fibo:
            if f==number:
                is_fibo_num=True
                break
        return is_fibo_num

fibo_instance=IsFibonacci()
print(fibo_instance.solution(8))
