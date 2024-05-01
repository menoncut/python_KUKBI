class Person:
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address
        
    def greeting(self):
        print('안녕하세요. 저는 {0}입니다.'.format(self.name))
        
    def attack(self):
        print('도술을 부려 바람을 일으켰습니다.')

    def runfast(self):
        print('축지법을 사용해 달립니다.')