# 1. 변수 할당과 참조의 변화
data = 100              # 정수형 객체 생성 및 data 변수가 이를 참조
print(f"초기 타입: {type(data)}")

data = "Algorithm"      # 이제 data는 문자열 객체를 참조함 (타입이 유연하게 변경됨)
print(f"변경 후 타입: {type(data)}")

data = "안녕하세요"      
print(f"변경 후 타입: {type(data)}")

# 2. 참조에 의한 객체 공유 (중요 개념)
list_a = [10, 20, 30]
list_b = list_a         # 동일한 메모리 주소를 공유함

print(f"list_a의 값: {list_a}")
print(f"list_b의 값: {list_b}")

list_b.append(40)       # b를 수정했으나
print(f"list_a의 상태: {list_a}")  # a도 함께 변경됨: [10, 20, 30, 40]
# 같은 주소를 공유하고 있어 변경됨
# list_b = list_a  == list_a = list_b