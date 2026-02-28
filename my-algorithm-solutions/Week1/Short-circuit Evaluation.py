#논리 연산과 단락 평가

# 단락 평가의 실전 사례
def check_status():
    print("시스템 상태 확인 중...")
    return True

# list_a가 비어있지 않을 때만 두 번째 조건을 확인하므로 에러를 방지함
items = []
if check_status() and items :
    print("아이템이 존재하며 시스템이 정상입니다.")
else:
    print("아이템이 없거나 확인을 생략했습니다.") # check_status()는 실행조차 안 됨