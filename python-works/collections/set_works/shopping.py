cart1={"milk","bread","egg","butter"}
cart2={"bread","juice","egg","chease"}
print("both cart:",cart1.union(cart2))
print("only cart1:",cart1.difference(cart2))
print("only cart2:",cart2.difference(cart1))
print("bouth at least once:",cart1.symmetric_difference(cart2))
