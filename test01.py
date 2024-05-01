stuck = {'삼각김밥':10,'커피우유':10}

# print(stuck)
# stuck = dict({'삼각김밥':10,
#          '커피우유':10,
#          '라면':10})
# print(stuck)


# key = input('추가할 상품을 입력하세요 : ')
# value = int(input('추가할 상품의 개수를 입력하세요 : '))

# if key in stuck:
    # plusStuck = stuck[key] + value
    # stuck[key] = plusStuck             추가 방법 1
    # stuck[key] = stuck[key] + value    추가 방법 2
    # stuck['라면'] = ['농심','삼양']
# print(stuck)



def add():    

 while True:

    key = input('추가할 상품을 입력하세요 : ')
    if key == "":
        break   

    value = int(input('추가할 상품의 개수를 입력하세요 : '))     
    
    if key in stuck:
        stuck[key] = stuck[key] + value
        print(f'{key} 상품이 {value}개 추가되었습니다.')
    else :
        stuck[key] = value
        print(f'{key} 신규 상품이 {value}개 추가등록 되었습니다.')
        
        
def sale():
    
 while True:
     
     sales = input('판매할 상품을 입력하세요 : ')
     
     if sales == "":
         break
     
     salesCount = int(input('판매할 상품의 개수를 입력하세요 : '))
     
     if stuck[sales] >= salesCount:
         stuck[sales] -= salesCount
         print(f'{sales} 재고가 {salesCount}갯수 만큼 차감되어 남은 수량은 {stuck[sales]}개 입니다.')
         
     elif stuck[sales] < salesCount:
         print(f'{sales} 상품의 재고가 부족합니다')
         
     else:
         print('찾으시는 제품이 없습니다.')
         
     
def printStuck():
    
 while True:
     
     stuckPrint = input('재고조회 하실 상품명을 입력하세요 : ')
     
     if stuckPrint == "":
         break
     
     if stuckPrint in stuck:
        print(f'{stuckPrint} : {stuck[stuckPrint]}EA')
        
     else:
        print('등록되지 않은 상품입니다.')
        
     
     
     
     
   
    
    # while key != " ":
    #     key = input('추가할 상품을 입력하세요 : ')
    #     break
    # if key == " ":
    #     print(stuck)
        
    # elif key != ' ':
    #     key = input('추가할 상품을 입력하세요 : ')
    #     value = int(input('추가할 상품의 개수를 입력하세요 : '))
    # elif key in stuck:
    #     stuck[key] = stuck[key] + value
    # elif key not in stuck:
    #     stuck[key] = value
            
        
        

        
        
    

while True:
    
    menuNum = int(input('1:재고등록 2:재품판매 3:재고조회 4:프로그램 종료\n원하시는 메뉴를 선택하세요 :'))
    
    if menuNum == 1:
        add()
    elif menuNum == 2:
        sale()
    elif menuNum == 3:
        printStuck()
    elif menuNum == 4:
        print('종료되었습니다.')
        break
    print('종료되었습니다.')
    

