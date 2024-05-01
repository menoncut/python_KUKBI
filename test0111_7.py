# for i in range(100):
#     print('hello world',(i+1))
    
# for i in range(5, 12):
#     print('hello world',i)

# for i in range(0,10,2):
#     print('hello world',i)

# for i in range(10,0,-1):
#     print('hello world',i)

# for i in reversed(range(10)):
#     print('hello world',i)

# count = int(input('반복할 횟수를 입력하세요 : '))

# for i in reversed(range(count)):
#     print('hello world',i)
    
입력값 = input("숫자와 문자를 입력하세요 (예: 10, apple): ")    

입력리스트 = 입력값.split()

print(입력리스트)

count = int(입력리스트[0])

문자 = 입력리스트[1]
print(문자)

for i in range(count):
    print(i,문자)
    
숫자 = int(입력리스트[0])
print(f'{숫자}번 실행')

    