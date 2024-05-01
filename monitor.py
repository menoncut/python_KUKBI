class Monitor:
    def __init__(self,brand,size):
        self.brand = brand
        self.size = size
        self.swith = 'ON'
        self.volume = 8
        self.content = ''  
        self.__serial_number = 'ABC123' 
    
    def swithOn(self):
        print('모니터의 전원을 켰습니다.')

    def swithOff(self):
        print('모니터의 전원을 껐습니다.')
        
    def 전원변경(self,elecswith):
        self.swith = elecswith
        print('전원이 {0} 되었습니다.'.format(self.swith))

    def 볼륨변경(self,volumechange):
        self.volume = volumechange
        print('모니터의 볼륨이 {0}로 변경되었습니다.'.format(self.volume))

    def 볼륨더하기10(self):
        self.volume += 10
        print('모니터의 볼륨이 {0}로 변경되었습니다.'.format(self.volume))

    def 볼륨빼기10(self):
        self.volume -= 10
        print('모니터의 볼륨이 {0}로 변경되었습니다.'.format(self.volume))
        
    def 화면표시(self,content):
        self.content = content
        if self.swith == 'ON':
            print('모니터에 다음 내용을 표시합니다.\n{0}'.format(self.content))
        elif self.swith == 'OFF':
            print('모니터가 꺼져있습니다. 먼저 모니터를 켜주세요.')
        
    def 시리얼_번호_확인(self):
        print('모니터의 시리얼 넘버 : \n',self.__serial_number) 
        
    def 시리얼_번호_확인1(self):
        return self.__serial_number

    def 시리얼_번호_변경(self,new_serial_number):
        self.__serial_number = new_serial_number
        print('모니터의 시리얼 넘버가 {0}로 변경되었습니다.'.format(self.__serial_number))       
        
        
lg_monitor = Monitor("Samsung",21)
print('모니터 브랜드 : ', lg_monitor.brand)
print('모니터 크기 : ', lg_monitor.size)
print('모니터 상태 : ', lg_monitor.swith)
print('모니터 볼륨 : ', lg_monitor.volume)

lg_monitor.swithOn()
lg_monitor.swithOff()

lg_monitor.전원변경('OFF')
lg_monitor.볼륨변경(15)

lg_monitor.전원변경('ON')
lg_monitor.볼륨변경(6)

lg_monitor.볼륨더하기10()
lg_monitor.볼륨더하기10()
lg_monitor.볼륨빼기10()

lg_monitor.화면표시('안녕하세요.')
lg_monitor.화면표시('배고파요.')
lg_monitor.전원변경('OFF')
lg_monitor.화면표시('밥주세요.')
lg_monitor.전원변경('ON')
lg_monitor.화면표시('밥주세요.')

lg_monitor.시리얼_번호_확인()
lg_monitor.시리얼_번호_변경('lg20240118_1')
lg_monitor.시리얼_번호_확인()

시리얼번호확인 = lg_monitor.시리얼_번호_확인1()
print('시리얼 넘버 확인 : ', 시리얼번호확인)




