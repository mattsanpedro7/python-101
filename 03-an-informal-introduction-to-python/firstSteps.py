# Fibo series
a, b = 0, 1
print(a, b)

while b < 20:
  print(b)
  a, b = b, a + b
  
i = 256 ** 2
print('The value of i is', i)

a, b = 0, 1
while b < 1000:
  print(b, end=',')
  a, b = b, a + b

print('\n')
