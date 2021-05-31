print('Введите натуральное число n:')
n = int(input())
cnt = 0
for i in range(1, n + 1):
    cnt += str(i).count('5')
print(cnt)
        
