##[기초] 변수와 연산자
#미션 1: 변수 타입과 형 변환 (Type Casting)

a = 10
b = "20"

result = a + int(b)
print(result)
print("--------------------------------")

#미션 2: 산술 연산과 비교 (Operators)

def cal(a, b):
  add = a + b 
  result_list.append(add)

  sub = a - b 
  result_list.append(sub)

  mul = a * b 
  result_list.append(mul)

  div = a // b 
  result_list.append(div)
  
def size(a, b):
  if a > b:
    return True
  else:
    return False

num1 = 10
num2 = 3
result_list = []

cal(num1, num2)
print(result_list, "\n", size(num1, num2), sep="")

print("--------------------------------")

## [제어] 조건문과 반복문
#미션 3: 조건에 따른 로직 분기 (If-Elif-Else)

scroe_list = ["A","B","C"]

score = 85

if score >= 90:
  print(scroe_list[0])

elif score >= 70:
  print(scroe_list[1])

elif not score > 70:
  print(scroe_list[2])

print("--------------------------------")


#미션 4: 범위 반복문 활용 (For Loop & Range)

# n = 5
# result = 0

# for i in range(0, 5):
#   result += n
#   n -= 1

# print(result)


n = 5
result = 0

for i in range(1, n+1):
  result += i

print(result)
print("--------------------------------")

##3. [문자열 & 리스트] 기초 조작
#미션 5: 문자열 포맷팅과 인덱싱 (String Formatting)

name = "Alice"
age = 25

print(f"My name is {name} and I am {age} years old.", name[0])

# 괄호를 한 번 더 써서 ( ) 묶어주면 튜플로 출력됨
print((f"My name is {name} and I am {age} years old.", name[0]))

print("--------------------------------")


#미션 6: 리스트 다루기 (List Operations)

my_list = []

for i in range(1, 4):
  my_list.append(i)

print(len(my_list))

print("--------------------------------")



