print("#1")
array = [273, 32, 103, "문자열", True, False]
print(array)
print([1, 2, 3, 4])
print(["안", "녕", "하", "세", "요"])
print([273, 32, 103, "문자열", True, False])
print()

print("#2")
list_a = [273, 32, 103, "문자열", True, False]
print(list_a)
print(list_a[0])
print(list_a[1])
print(list_a[2])
print(list_a[1:3])
print()

print("#3")
list_a[0] = "변경"
print(list_a)
print()

print("#4")
print(list_a)
print(list_a[-1])
print(list_a[-2])
print(list_a[-3])
print()

print("#5")
print(list_a)
print(list_a[3])
print(list_a[3][0])
print()

print("#6")
list_a = [[1,2,3],[4,5,6],[7,8,9]]
print(list_a)
print(list_a[1])
print(list_a[1][1])
print()

print()
list_a = [1,2,3,4,5]
1 in list_a
99 in list_a
3 not in list_a
6 not in list_a