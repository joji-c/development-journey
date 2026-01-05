text="this is a python programming for word count this program is simple"
lis=text.split()
wc={ch:lis.count(ch) for ch in lis}
print(wc)