print('Введите натуральное число n:')
n = int(input())
d = 2
while n >= 2 and n % d != 0:
    d += 1
if n == d:
    print('Yes')
else:
    print('No')