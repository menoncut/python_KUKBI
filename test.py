# file = open('hello.txt', 'w')
# file.write('hello, world!')
# file.close()
# print('입력이 파일에 저장되었습니다.')

# str = input('문자열을 입력하세요 : ')
# file = open('str.txt', 'w', encoding="utf-8") # w를 a로 바꾸면 w로 쓴 문자열 뒤에 추가할 수 있다.
# file.write(str)
# file.close()

# file = open('hello.txt', 'r')
# s = file.read()
# print(s)
# file.close()

# readopen = input('읽을 파일명을 입력하세요 : ')
# file = open(readopen, 'r')
# s = file.read()
# print(s)
# file.close()

# use_in = input('저장내용 입력하세요 : ')
# with open('test.txt', 'w') as file:
#     file.write(use_in)
#     print('입력이 파일에 저장되었습니다.')
    
# with open('hello2.txt', 'w') as file:
#     for i in range(3):
#         file.write('hello, world! {0}\n'.format(i))

# -------------------------------------------------------------
        
# lines = ['안녕하세요.\n', '파이썬\n', '코딩 도장입니다.\n']        

# with open('hello2.txt', 'w', encoding="utf-8") as file:
#     file.writelines(lines)    

# -------------------------------------------------------------
    
# while True:    
#     w = input('안녕하세요 (x를 누르면 종료됩니다.)')    

#     if w != 'x':

#         with open('hello3.txt', 'w', encoding="utf-8") as file:
#             file.write(w)
#         print('입력이 파일에 저장되었습니다.')
#     elif w == 'x':
#         print('종료되었습니다.')
        
# -------------------------------------------------------------
        
# print('여러 줄을 입력하세요. 입력을 종료하려면 빈 줄에서 엔터를 누르세요')
# content = ""        
# while True:
#         line = input()
#         if line == '':
#             break
#         content += line +'\n'

# with open('abc.txt', 'w', encoding="utf-8") as file:
#         file.write(content)
# print('입력한 내용이 abc.txt 파일에 저장되었습니다.')

# -------------------------------------------------------------

end = ''

while end != 4:

    print('==========파일관리==========\n'),
    print('1. 파일 만들기\n'),
    print('2. 여러줄 입력하기\n'),
    print('3. 원하는 파일 읽어오기\n'),
    print('4. 종료\n')   
    
    print('메뉴를 선택하세요 : ')
    
    choice = int(input())

    if choice == 1:
        filename = input('파일명을 입력하세요(파일명.txt) : ')
        content = input('파일에 저장할 내용을 입력하세요 : ')
        
        with open(filename, 'w', encoding="utf-8") as file:
            file.write(content)
        print(f'입력한 내용이 {filename} 파일에 저장되었습니다.')

    elif choice == 2:
        filename = input('파일명을 입력하세요(파일명.txt) : ')         
        content = ""        
        while True:
            line = input('여러 줄을 입력하세요. 입력을 종료하려면 빈 줄에서 엔터를 누르세요\n')
            if line == '':
                print('입력이 종료되었습니다.')
                break
            content += line +'\n'

        with open(filename, 'w', encoding="utf-8") as file:
            file.write(content)
            print(f'입력한 내용이 {filename} 파일에 저장되었습니다.')
    
    # elif choice == 3:
    #     readopen = input('읽을 파일명을 입력하세요(파일명.txt) : ')
    #     file = open(readopen, 'r')
    #     s = file.read()
    #     print(s)
    #     file.close()
    
    elif choice == 3:
        readopen = input('읽어올 파일명을 입력하세요 : ')
        try:
            with open(readopen, 'r') as file:
                content = file.read()
                print(f'{readopen} 파일의 내용 :')
                print(content)
        except FileNotFoundError:
            print(f'{readopen}파일을 찾을 수 없습니다.')
        
    elif choice == 4:
        end = 4
        print('프로그램이 종료되었습니다.')
        
# -------------------------------------------------------------


    
    



        

        

    

