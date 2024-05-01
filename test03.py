# def ten_div(x):
#     return 10 / x

# print(ten_div(0))

# -------------------------------------------------------------------------------------------------------

try:
    x = int(input('나눌 숫자를 입력하세요 : '))
    y = 10 / x
    print(y)
except ZeroDivisionError:
    print('숫자를 0으로 나눌 수 없습니다.')    # ZeroDivisionError 에 해당하는 에러가 발생하면 "숫자를 0으로 나눌 수 없습니다." 를 실행하고 해당하지 않으면 그 아래 Exception으로 내려가 예외처리를 한다.(Exception은 모든 예외처리를 처리해준다.)
except ValueError:
    print('숫자만 입력할 수 있습니다.')    
except Exception as e:
    print('예외가 발생했습니다.', e)
else:
    print(y)
    
    
