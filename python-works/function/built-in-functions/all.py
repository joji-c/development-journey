lst=[10,11,12,13,14,15]
even_num=[n%2==0 for n in lst]
#ev_num=list(map(lambda n:n%2==0,lst))
all_even=all(even_num)
print(all_even)

above_nine=[n>9 for n in lst]
#ab_nine=list(map(lambda n:n>9,lst))
all_above_nine=all(above_nine)
print(all_above_nine)
