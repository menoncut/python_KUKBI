import calcpkg.operation  # calcpkg 패키지의 operation 모듈을 가져옴
import calcpkg.geometry  # calcpkg 패키지의 geometry 모듈을 가져옴

print(calcpkg.operation.add(10,20))  # operation 모듈의 add 함수를 가져옴
print(calcpkg.operation.mul(10,20))  # operation 모듈의 mul 함수를 가져옴

print(calcpkg.geometry.triangle_area(30,40))  # geometry 모듈의 triangle_area 함수를 가져옴
print(calcpkg.geometry.rectangle_area(30,40))  # geometry 모듈의 rectangle_area 함수를 가져옴

# __init__.py 파일(모듈)이 들어있는 폴더는 자동으로 패키지 폴더로 인식된다.(__init__.py 에는 아무 내용도 입력하지 않아도 된다.)
# 'calcpkg' 폴더를 만든 후 __init__.py, geometry.py, operation.py 모듈을 만들고 main.py 모듈은 만드는데 중요한 것은 'calcpkg' 폴더 바깥에 위치
# 시켜야 한다.


