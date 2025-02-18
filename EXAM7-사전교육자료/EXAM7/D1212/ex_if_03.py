# 제어문-조건문
# - 목적: 조건에 따라 실행되는 코드가 다름
# - 종류: (단일)조건문, 다중조건문, 중첩조건문
# [다중 조건문]
# 숫자를 입력받아서 양수, 0, 음수에 따라 출력
# 구분방법: 숫자>0, 숫자<0, 숫자==0
# 출력형태: 6은 양수입니다. -2는 음수, 0은 0입니다.
num=int(input('숫자를 입력해주세요:'))
if num>0:
    print(f'{num}은 양수입니다.')
elif num<0:
    print(f'{num}은 음수입니다.')
else:
    print(f'{num}은 0입니다.')