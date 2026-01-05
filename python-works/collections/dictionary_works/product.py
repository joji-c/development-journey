product={"code":1234,
         "title":"amul choco bar",
         "catogery":"frozen goods",
         "price":80,
         "avl_qnty":20}

#check if price key exist
if "price" in product:
    print(product["price"])
else:
    print("key not exist")

#if avl_qnt exist add 10 else add 15
if "avl_qnty" in product:
    product["avl_qnty"]+=10
else:
    product["avl_qnty"]=15
print(product)
