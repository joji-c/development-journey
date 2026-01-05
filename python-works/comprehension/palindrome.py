words=["radar","level","dam","madam","act","cat","radar","level","madam","malayalam"]
palin={ch:words.count(ch) for ch in words if ch==ch[::-1]} 
print(palin)