#데이터 형 변환과 예외 처리 (Type Casting)

# 사용자의 입력을 정수로 변환하는 예시
raw_input = "25"        # 문자열 데이터
age = int(raw_input)    # 정수형으로 명시적 변환
next_year_age = age + 1 # 이제 산술 연산이 가능함
print(f"처음 나이: {raw_input}")
print(f"변환 후 나이 {next_year_age}")

# 수치형 간의 변환
pi = 3.14159
integer_pi = int(pi)    # 소수점 아래를 버리고 정수 3만 취함
print(f"정수 변환 결과: {integer_pi}")


#형 변환 시 발생할 수 있는 오류 (ValueError)
user_data = "2024년"

try:
    # 숫자가 아닌 문자가 포함되어 있어 에러 발생 가능성이 높음
    converted_data = int(user_data)
except ValueError:
    # 에러 발생 시 프로그램 종료 대신 대체 로직 수행
    print("수치형 데이터로 변환할 수 없는 형식입니다. 전처리가 필요합니다.")