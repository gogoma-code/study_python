output_a = "{:f}".format(52.273)
output_b = "{:15f}".format(52.273)
output_c = "{:+15f}".format(52.273)
output_d = "{:+015f}".format(52.273)
print("float 자료형 기본")
print(output_a)
print(output_b)
print(output_c)
print(output_d)
print()

output_a = "{:.3f}".format(52.273)
output_b = "{:.2f}".format(52.273)
output_c = "{:.1f}".format(52.273)
print("소수점 아래 자릿수 지정")
print(output_a)
print(output_b)
print(output_c)
print()

output_a = 52.0
output_b = "{:g}".format(output_a)
print("의미 없는 소수점 제거")
print(output_a)
print(output_b)
print()

a = "Hello Python Programming...!"
print("대소문자 바꾸기")
print(a.upper())
print(a.lower())
print()

b = """
    안녕하세요
문자열의 함수를 알아봅니다.
"""
print("문자열 양옆의 공백 제거하기: strip()")
print(b)
print(b.strip())
print()

print("TrainA10".isalnum())
print("10".isdigit())
print()

output_a = "안녕안녕하세요".find("안녕")
print(output_a)
output_b = "안녕안녕하세요".rfind("안녕")
print(output_b)
print()

print("안녕" in "안녕하세요") #True
print("잘자" in "안녕하세요") #False
print()

a = "10 20 30 40 50".split(" ")
print(a)