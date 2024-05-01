class Foodorder:
    def __init__(self,고객이름,고객주문):
        self.고객이름 = 고객이름
        self.고객주문 = 고객주문
        
    def orderInfo(self):        
        print(f'고객이름 : {self.고객이름} / 주문한 햄버거 : {self.고객주문}')
        print('주문이 완료되었습니다. 감사합니다.')
        
    def orderPrice(self):
        if self.고객주문 == "치즈버거":
            price = 5000
        elif self.고객주문 == "불고기버거":
            price = 3000    
        elif self.고객주문 == "와퍼버거":
            price = 7900    
        elif self.고객주문 == "새우버거":
            price = 6900    
        print(f'주문하신 {self.고객주문}의 가격은 {price}원 입니다.')
        
        
        
        