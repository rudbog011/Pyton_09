print('Введите натуральное число n:')
n = int(input())
summ = 0
while True:
    while n != 0:
        summ = summ + (n % 10)
        n = n // 10
    n = summ
    summ = 0
    if n < 10:
        break
print(n)
    