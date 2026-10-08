# distionary comprehension is same as list comprehension but retrun key value PendingDeprecationWarning
# {key:value for_in_loop}
# { key:value  for_in_loop if_condition}
# { key:ternaryoperator for_in_loop}



square = {el:el*el  for el in [1,2,3]}
print(square)



evenSquare  = {el:el*el  for el in [1,2,3,4] if el%2==0}
print(evenSquare)


countLetter  ={ el:len(el)  for el in ["nitan", "ram","hari"]}
print(countLetter)



evenOdd = {el:"even" if(el%2==0) else "odd"  for el in [1,2,3,4,5]}

print(evenOdd)