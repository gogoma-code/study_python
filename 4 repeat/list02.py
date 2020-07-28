list_a = [1,2,3]

print("#리스트 뒤에 요소 추가")
print(list_a)
list_a.append(4)
list_a.append(5)
print(list_a)
print()

print("#리스트 중간에 요소 추가")
print(list_a)
list_a.insert(0, 10)
list_a.insert(2, 11)
list_a.insert(1, 12)
print(list_a)
print()

print("#한 번에 여러 요소 추가")
list_a = [1,2,3]
print(list_a)
list_a.extend([4,5,6])
print(list_a)
print()

print("#리스트 연결 연산자와 요소 추가의 차이")
list_a = [1,2,3]
list_b = [4,5,6]
list_a + list_b #[1, 2, 3, 4, 5, 6]

list_a.extend(list_b)
list_a #[1, 2, 3, 4, 5, 6]
list_b #[4, 5, 6]
