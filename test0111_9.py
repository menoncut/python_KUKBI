# i = 0
# sum = 0
# while i < 100:
#     print('hello world',i)
#     i += 1
#     sum += i
    
# print(sum)

# i = 0
# while True:
#     print(i)
#     i += 1
#     if i == 100:
#         break

sum = 0
for i in range(100):
    if i % 2 == 0:
        continue
    sum += i
    print(sum)