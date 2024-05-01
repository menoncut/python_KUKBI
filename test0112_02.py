# a = [10, 20, 30]
# a.append(500)
# print(a)
# print(len(a))

# a = [10,20,30]
# a.append([50,60])
# print(a)
# print(len(a))

# a = [10,20,30]
# a.extend([50,60])
# print(a)
# print(len(a))

# a = [10,20,30]
# a.insert(2,60)
# print(a)
# print(len(a))

# a = [10,20,30]
# a.pop()
# print(a)
# print(len(a))

# a = [10,20,30]
# a.pop(1)
# print(a)
# print(len(a))

# a = [10,20,30]
# del a[1]
# print(a)
# print(len(a))

# a = [10,20,30]
# a.remove(20)
# print(a)
# print(len(a))

# a = [10,20,30,40,50]
# print(a.index(20))

# a = [10,20,30,40,50,20,20,20]
# print(a.count(20))

# a = [10,20,30,40,50,20,20,20]
# a.reverse()
# print(a)

# a = [10,20,30,40,50,20,20,20]
# a.sort()
# print(a)

# a = [10,20,30,40,50,20,20,20]
# a.sort(reverse=True)
# print(a)

# a = [10,20,30,40,50,20,20,20]
# a.clear()
# print(a)

# a = [10,20,30,40,50,20,20,20]
# del a[1:4]
# print(a)

# ------------------------------


# a = [0,0,0,0,0]
# b=a

# b[2] = 99
# print(a)
# print(b)

# print(a is b)

# ------------------------------

# a = [0,0,0,0,0]
# b = a.copy()
# print(b)

# print(a is b)
# print(a == b)

# a[2] = 99
# print(a)
# print(b)

# ------------------------------

# a = [38, 21, 53, 62, 19]
# for index, value in enumerate(a):
#     print(index, value)
    
# --------------------------------------------------------------------------------

fruits = ['apple', 'banana', 'cherry', 'orange']

fruit = input('추가할 과일을 선택하세요 : ')
fruits.append(fruit)
print(fruits)

delfruit = input('삭제할 과일을 입력하세요 : apple, banana, cherry, orange) ')
fruits.remove(delfruit)
print(fruits)

position, fruit_name = input('추가할 위치와 과일을 입력하세요 : (예:3 수박)').split()

fruits.insert(int(position), fruit_name)
print("업데이트된 과일 리스트 : ", fruit_name)
print(f'{fruit_name}을(를) 리스트의 {position}번째 위치에 추가하였습니다.')
print(fruits)

# --------------------------------------------------------------------------------











