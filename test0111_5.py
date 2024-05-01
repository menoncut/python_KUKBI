import random
가위바위보 = ['가위','바위','보']

while True:
    사용자 = input("가위, 바위, 보 중에 선택하세요 : ")

    컴퓨터 = random.choice(가위바위보)

# 결과 출력
    print("사용자", 사용자)
    print("컴퓨터", 컴퓨터)

# 승패 결정
    if 사용자 == 컴퓨터:
        print("비겼습니다.")
    elif (사용자 == "가위" and 컴퓨터 == "보")or(사용자 == "바위" and 컴퓨터 == "가위")or(사용자 == "보" and 컴퓨터 == "바위"):
        print("당신이 이겼습니다.")
    else:
        print("당신이 졌습니다.")
