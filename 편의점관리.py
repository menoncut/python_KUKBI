def add():
    while True:
        product_name = input("추가할 상품명을 입력하세요 (엔터키 입력 시 종료): ")
        if product_name == "":
            break

        quantity_input = input("추가할 개수를 입력하세요: ")
        if quantity_input == "":
            print("잘못된 입력입니다. 다시 시도해주세요.")
            continue

        quantity = int(quantity_input)

        if product_name in inventory:
            inventory[product_name] += quantity
            print(f"{product_name}의 개수가 {quantity}개 추가되었습니다.")
        else:
            inventory[product_name] = quantity
            print(f"{product_name}이(가) 재고에 {quantity}개 추가되었습니다.")
            print()
            
    print()
    print("=== 재고 현황 ===")
    for product, count in inventory.items():
        print(f"{product}: {count}개")
    print()
        
        
def sale():
    while True:
        product_name = input("판매할 상품명을 입력하세요 (엔터키 입력 시 종료): ")
        if product_name == "":
            break

        if product_name in inventory:
            quantity = int(input("판매할 개수를 입력하세요: "))

            if inventory[product_name] >= quantity:
                inventory[product_name] -= quantity
                print(f"{product_name}의 개수가 {quantity}개 판매되었습니다.")
                print(f"남은 개수: {inventory[product_name]}개")
            else:
                print("재고가 부족합니다.")
        else:
            print("찾으시는 제품이 없습니다.")

def view():
    while True:
        product_name = input("조회할 상품명을 입력하세요 (엔터키 입력 시 종료): ")
        if product_name == "":
            break

        # if product_name in inventory:
        #     quantity = inventory[product_name]
        #     print(f"{product_name}의 개수: {quantity}개")
        if product_name in inventory:
            qu = inventory[product_name]
            print(f"{product_name}의 개수: {qu}개")



        else:
            print("등록되지 않은 상품입니다.")


inventory = {
    '삼각김밥': 10,
    '커피우유': 10
}


while True:
    print("===== 편의점 재고 관리 프로그램 =====")
    print("1: 재고_등록")
    print("2: 제품_판매")
    print("3: 재고_조회")
    print("0: 프로그램_종료")

    choice = input("메뉴를 선택하세요: ")

    if choice == "1":
        add()

    elif choice == "2":
        sale()

    elif choice == "3":
        view()

    elif choice == "0":
        print("프로그램을 종료합니다.")
        break

    else:
        print("잘못된 입력입니다. 다시 선택하세요.")