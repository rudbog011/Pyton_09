print('Введите натуральное число n:')
n = int(input())
count = 0
for i in range(1, n + 1):
    if '5' in str(i):
        count += 1
print(count)
        
