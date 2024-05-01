# while True:
#     num = int(input('숫자를 입력하세요 : '))

#     if num >= 0:
#         print('양수입니다.')
#     elif num < 0:
#         print('음수입니다.')


# while True:    
#         계절목록 = {
#         '봄':'봄은 꽃이 피는 계절입니다.',
#         '여름':'여름은 더운 날씨입니다.',
#         '가을':'가을은 천고마비의 계절입니다.',
#         '겨울':'겨울엔 눈이 내립니다.'            
#         }

#         선호계절 = input('좋아하는 계절을 입력하세요 : ')

#         if 선호계절 in 계절목록:
#                 # 계절특징 = 계절목록[선호계절]
#                 print(계절목록[선호계절])
#         else:
#                 print("잘못된 입력입니다. '봄', '여름', '가을', '겨울' 중 하나를 입력해주세요.")


# season = input('사계절중 하나를 입력하세요 : (봄, 여름, 가을, 겨울)')

# if season == '봄':
#     print('봄은 꽃이 피는 계절입니다.')
# elif season == '여름':
#     print('여름은 더운 계절입니다.')
# elif season == '가을':
#     print('가을은 천고마비 계절입니다.')
# elif season == '겨울':
#     print('겨울은 추운 계절입니다.')
# else:
#     print('잘못된 입력입니다.')
   

# while True:                
#         과일리스트 = ['사과','바나나','체리','딸기','포도']

#         선호과일 = input('선호하는 과일을 입력하세요 : ')

#         if 선호과일 in 과일리스트:
#                 print(f'{선호과일}은(는) 리스트에 있습니다.')
#         else:
#                 print(f'{선호과일}은(는) 리스트에 없습니다.')

# while True:
#     strchoice = input('문자열을 입력하세요 : ')        
#     strsearch = "금요일"

#     if strsearch in strchoice:
#         print("입력한 문자열에 '금요일' 이 포함되어 있습니다.")
#     else:
#         print("입력한 문자열에 '금요일' 이 포함되어 있지 않습니다.")
    
# num = [0,1,2,3,4,5,6,7,8,9]

# print(num[2:7])

# for i in range(1, 100):
#     print(i)
    
# fruits = ["사과", "바나나", "참외"]
# for fruit in fruits:
#     print(fruit)

# num = int(input('양수를 입력하세요 : '))
# sum = 0
# count = 1

# while count <= num:
#     sum += count
#     count += 1
    
#     print(f'1부터 {num}까지의 합은 {sum}입니다.')
    
# for i in range(5):
#     for j in range(5):
#             print('j:', j, sep='', end='')
#     print('i:', i, '\\n', sep='')

# for i in range(5):
#     for j in range(5):
#         print('*', end='')
#     print()
    
#     for i in range(5):
#         for j in range(5):
#             if j <= i:
#                 print('*', end='')
#         print()
        
# for i in range(5):
#     for j in range(5):
#         if j == i:
#             print('*', end='')
#         print()
        
# for i in range(5):
#     for j in range(5):
#         if j == i:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()
    
# while True:
#     인공지능 = {'안녕':'안녕하세요',
#             '넌 누구니?':'나는 인공지능이야.',
#             '왜 반말이야':'너도 반말하자나.',
#             '오늘의 계절은?':'오늘은 맑아'    
#     }

#     질문 = input('인공지능과 대화하세요 : ')

#     if 질문 in 인공지능:
#         print(인공지능[질문])
    
#     else:
#         print('죄송합니다. 질문을 이해하지 못했습니다.')


    