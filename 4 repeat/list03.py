list_a = [0, 1, 2, 3, 4, 5]

print("#리스트의 요소 하나 제거하기")
print("#제거방법[1] - del")
print(list_a)
del list_a[1]
print(list_a)
print()

print("#제거방법[2] - pop()")
print(list_a)
list_a.pop(2)
print(list_a)
print()

list_a = [0, 1, 2, 3, 4, 5, 6]
print(list_a)
del list_a[3:6]
print(list_a)
print()

list_a = [0, 1, 2, 3, 4, 5, 6]
print(list_a)
del list_a[3:]
print(list_a)
print()

list_a = [0, 1, 2, 3, 4, 5, 6]
print(list_a)
list_a.remove(2)
print(list_a)
print()

print(list_a)
list_a.clear()
print(list_a)
