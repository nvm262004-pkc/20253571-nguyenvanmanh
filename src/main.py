# 버전 2: 점수 시스템 및 멀티 라운드 게임 플레이 추가

import random

# 프로그램 시작 메시지
print("--- 가위바위보 게임에 오신 것을 환영합니다! ---")
print("3점을 먼저 내는 사람이 최종 승리합니다!")

player_score = 0
computer_score = 0
winning_score = 3

while player_score < winning_score and computer_score < winning_score:
    print("\n--------------------------------")
    # 현재 점수 출력
    print(f"현재 점수: 당신 {player_score} - {computer_score} 컴퓨터")
    
    # 사용자로부터 선택 입력받기
    player_choice = input("선택하세요 (가위, 바위, 보): ").lower()
    
    # 유효한 입력인지 확인
    choices = ['가위', '바위', '보']
    if player_choice not in choices:
        print("잘못된 입력입니다. 다시 선택해주세요.")
        continue

    # 컴퓨터는 무작위로 선택
    computer_choice = random.choice(choices)

    print(f"\n당신의 선택: {player_choice}")
    print(f"컴퓨터의 선택: {computer_choice}\n")

    # 승자 결정 로직
    if player_choice == computer_choice:
        print("이번 라운드: 무승부!")
    elif (player_choice == '바위' and computer_choice == '가위') or \
         (player_choice == '가위' and computer_choice == '보') or \
         (player_choice == '보' and computer_choice == '바위'):
        print("이번 라운드: 당신의 승리!")
        player_score += 1
    else:
        print("이번 라운드: 당신의 패배!")
        computer_score += 1

# 게임 종료 메시지
print("\n--- 게임 종료 ---")
if player_score > computer_score:
    print("🎉 축하합니다! 최종 승리자는 당신입니다! 🎉")
else:
    print("아쉽지만 컴퓨터가 승리했습니다. 다음 기회에 행운을 빕니다!")
