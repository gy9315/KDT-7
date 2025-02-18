# 제어문 - 조건문
# - 특정 조건에 맞을 시 실행되는 경우와 실행되지 않는 코드 구분 실행
# [문] 숫자 2개 입력 받아서 덧셈 결과를 출력하세요
num1=input('숫자 1개 입력해주세요:').strip()
num2=input('숫자 1개 입력해주세요:').strip()
# 입력데이터 존재 여부 확인
# - 입력 했고, 숫자면 덧셈 연산 진행
# - 그 이후 다시 진행과 '잘못된 데이터입니다.'메시지 출력
if (len(num1)!=0)&(len(num2)!=0)&num1.isdigit()&num2.isdigit():
    print(int(num1)+int(num2))
else:
    print('잘못된 데이터입니다.')


