#산술 연산자의 정밀한 활용

# 나눗셈 연산의 구분
total = 10
count = 3

print(f"실수 나눗셈: {total / count}")   # 3.333... (정밀한 결과)
print(f"몫 연산(//): {total // count}")  # 3 (소수점 버림, 인덱스 계산 시 주로 사용)
print(f"나머지 연산(%): {total % count}") # 1 (짝홀 판별, 주기성 계산에 필수)

# 연산자 우선순위 활용
# 곱셈과 나눗셈이 덧셈보다 먼저 계산되나, 가독성을 위해 괄호를 권장함
result = (total + 5) * (count ** 2)      # 15 * 9 = 135
print(f"total + count = {result}")