print('Введите целое число:')
n = int(input())
while True:
    if n >= 10:
        if n <= 100:
            print(n)
        else:
            break
    n = int(input())