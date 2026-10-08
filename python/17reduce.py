num = [3,3,3]

from functools import reduce 
#reduce(function, sequence, initial)

def fun(pre,cur):
    return pre+cur

add = reduce(fun,num,0)
print(add)


pro = reduce(lambda pre,cur:pre*cur,num,1 )
print(pro)



products = [
    {"name":"laptop","price":1000},
    {"name":"mobile","price":2000},
    {"name":"tablet","price":3000}
]


totalProduct = reduce(lambda pre,cur: pre+cur["price"],products,0)
print(totalProduct)