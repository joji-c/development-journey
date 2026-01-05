file_path="python-works\\file_works\\word-count\\story.txt"
fr=open(file_path,"r")
count={}
for line in fr:
    line=line.rstrip("\n")
    line=line.split(" ")
    for word in line:
        word=word.rstrip(",")
        word=word.rstrip(".")
        if word in count:
            count[word]+=1
        else:
            count[word]=1
print(count)


max_val=max(count.values())
max_count={k:v for k,v in count.items() if v==max_val}
print(max_count)


fr.close()
