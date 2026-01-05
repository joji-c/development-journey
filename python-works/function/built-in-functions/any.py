lst1=["houseful","beautiful","peaceful","harmful","thankful","powerful"]
end_full=list(map(lambda w:w.endswith("full"),lst1))
any_end_full=any(end_full)
print(any_end_full)

lst2=["program","problem","perfect","apple"]
start_pro=[w.startswith("pro") for w in lst2]
any_start_pro=any(start_pro)
print(any_start_pro)

#prime num or not
number=11
print(number,"is prime:",not any([number%i==0 for i in range(2,number)]))
