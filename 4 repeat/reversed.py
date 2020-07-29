list_a = [1,2,3,4,5]
list_reversed = reversed(list_a)

print("list_a", list_a)
print("list_reversed", list_reversed)
print("list(list_reversed)", list(list_reversed))
print()

for i in reversed(list_a):
    print("-", i)