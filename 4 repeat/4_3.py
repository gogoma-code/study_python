a = range(5)
print(a)
print(list(range(10)))
print(list(range(0, 5)))
print(list(range(5, 10)))
print(list(range(0, 10, 2)))
print(list(range(0, 10, 3)))
print()

a = range(0, 10+1)
print(list(a))
print()

n = 10
a = range(0, int(n / 2))
print(list(a))
a = range(0, n // 2)
print(list(a))
print()

array = [273, 32, 103, 57, 52]
string = ""
for ele in array:
    string += str(ele) + " "
print(string)
print()

array = [273, 32, 103, 57, 52]
for i in range(len(array)):
    print("{}번째 반복: {}".format(i, array[i]))

