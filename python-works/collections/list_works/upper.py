def case(lower):
    upper=[]
    for l in lower:
        str1=str(l.upper())
        upper.append(str1)
    return upper

lower=["hello","how","are","you"]
print(case(lower))
