file_path="python-works\\error-handling\\numbers.txt"

try:
    fr=open(file_path,"r")

    lst=[]
    for line in fr:
        line=line.rstrip("\n")
        try:
            line=int(line)
            lst.append(line)
        except Exception as e:
            continue

    print("sum of numbers:",sum(lst))
    print("max number:",max(lst))
    print("min number:",min(lst))
    freq={n:lst.count(n) for n in lst}
    max_frequency={k:v for k,v in freq.items() if v==max(freq.values())}
    print("most repeated number:",max_frequency)

except Exception as e:
    print(e)
finally:
    fr.close()
    
