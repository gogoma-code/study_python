number = input("정수 입력> ")
number = int(number)

print("#1")
if number % 2 == 0:
    print("짝수")
if number % 2 == 1:
    print("홀수")

print("#2")
if number % 2 == 0:
    print("짝수")
else:
    print("홀수")
