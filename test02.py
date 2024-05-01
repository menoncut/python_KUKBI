def count_consecutive_zeros(num):
    count = [num[i] == num[i+1] == '0' for i in range(0, int(len(num)-1))].count(True)
    
count_consecutive_zeros(10010100101001110000)

