a = any([True, False, True])
print(a)


b = all([True, True, True])
print(b)

l = [2,4,6,1]


is_all_even= all([el%2==0  for el in l])
print(is_all_even)