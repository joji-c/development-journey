word="abbaacd"
rec={}
for ch in word:
    if ch in rec:
        print(ch,"is first recursive")
        break
    else:
        rec[ch]=1
