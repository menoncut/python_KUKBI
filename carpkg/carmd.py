class Car:
    def __init__(self,brand,name,madeyear):
        self.brand = brand
        self.name = name
        self.madeyear = madeyear
        
    def carinfo(self):
        print(f'{self.madeyear}년식 {self.brand} {self.name}')
        
    def enginestart(self):
        print('엔진이 시작되었습니다.')
        
    def engineoff(self):
        print('엔진이 정지되었습니다.')
        
        
        