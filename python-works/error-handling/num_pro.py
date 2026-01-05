file_path="python-works\\error-handling\\ev_num.txt"
fr=open(file_path,"r")

eve=[]
for line in fr:
    line=line.rstrip("\n")
    try:
        if line.isdigit() and int(line)%2==0:
            eve.append(line)
    except Exception as e:
        print(e)

print(eve)

eve_count={e:eve.count(e) for e in eve}
max_count={k:v for k,v in eve_count.items() if v==max(eve_count.values())}

print(max_count)
