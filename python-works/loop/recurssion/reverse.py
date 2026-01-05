def rev(num):
    if num==0:
        return ""
    return str(num%10) + str(rev(num//10))

print(rev(543))
