b = float(input('Enter decimal number'))

n = int(input('Enter an integer'))

x = 1 + b

for i in range(2, n+1):
    x += b** i

j = (b ** (n+1))/ (b-1)

print('sum', x)

print('sum', j)
