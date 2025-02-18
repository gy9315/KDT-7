# 연산자(Operator) - 객체 참조 카운팅
# - 객체: 메모리 힙 영역에 존재하는 데이터
# - 객체의 주소를 저장한ㄴ다 => 참조한다: 참소변수 reference variable
# --------------------------------------------------------------
# 기본 내장 builtins.py 제와한 나머지 파일들 가져와서 쓰기
import sys
# --------------------------------------------------------------
# 2025 데이터의 참조 카운트 출력
print(f'2025의 참조 카운트: {sys.getrefcount(2025)}')
a=2025
print(f'2025의 참조 카운트: {sys.getrefcount(2025)}')
b=2025
print(f'2025의 참조 카운트: {sys.getrefcount(2025)}')
c=2025
print(f'2025의 참조 카운트: {sys.getrefcount(2025)}')
# --------------------------------------------------------------
# 데이터 주소 저장하는 변수 삭제: del 변수명
del a
print(f'2025의 참조 카운트: {sys.getrefcount(2025)}')
del c
print(f'2025의 참조 카운트: {sys.getrefcount(2025)}')