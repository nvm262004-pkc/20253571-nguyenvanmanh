# 버전 1: 단판 승부

import random

# 프로그램 시작 메시지
print("--- 가위바위보 게임에 오신 것을 환영합니다! ---")

# 사용자로부터 선택 입력받기
player_choice = input("선택하세요 (가위, 바위, 보): ")

# 컴퓨터는 무작위로 선택
choices = ['가위', '바위', '보']
computer_choice = random.choice(choices)

print(f"\n당신의 선택: {player_choice}")
print(f"컴퓨터의 선택: {computer_choice}\n")

# 승자 결정
if player_choice == computer_choice:
    print("결과: 무승부!")
elif (player_choice == '바위' and computer_choice == '가위') or \
     (player_choice == '가위' and computer_choice == '보') or \
     (player_choice == '보' and computer_choice == '바위'):
    print("결과: 당신의 승리!")
elif player_choice not in choices:
    print("잘못된 입력입니다. '가위', '바위', '보' 중에서 하나를 선택해야 합니다.")
else:
    print("결과: 당신의 패배!")