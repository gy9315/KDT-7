# 제어문 while 반복문
# - 반복횟수가 미정인 경우에도 사용 가능
# - 반복횟수가 정해진 경우에도 사용 가능함
# ----------------------------------------------------
# 반복 횟수가 정해지지 않은 경우
# 임의 숫자 설정
num=7
while True:
    num1=input('맞춰봐! 숫자입력(범위: 1 ~ 20):')
    if num==int(num1):
        print('bingo')
        break