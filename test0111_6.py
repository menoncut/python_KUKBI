import random

while True:
    정답 = random.randint(1,5)

    추측 = int(input("1부터 5까지 숫자 중 하나를 맞춰보세요: "))

    if 추측 == 정답:
        print("정답입니다.")
        
    elif 추측 < 정답:
        print("정답은 더 큽니다.")
    else:
        print("틀렸습니다.",정답,"입니다.")
