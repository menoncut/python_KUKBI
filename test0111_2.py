음료수_목록 = {
        '콜라':1500,
        '사이다':1200,
        '환타':100,
        '웰치스':1300,
        '아메리카노':200
}

while True:
    print("자판기 음료수 목록: ")
    for 음료, 가격 in 음료수_목록.items():
        print(f'{음료}:{가격} 원')

    입력_음료 = input('어떤 음료를 선택하시겠습니까?')

    if 입력_음료 in 음료수_목록:
        가격 = 음료수_목록[입력_음료]
        print(f'{입력_음료}를 선택하셨습니다.{가격}원을 결제해주세요.')
    elif 입력_음료 == '커피':
        print('커피는 옆집 컴포즈를 이용하세요.')
    else:
        print(f'죄송합니다. {입력_음료}는 없습니다.')