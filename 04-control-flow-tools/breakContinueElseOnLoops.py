# use of break statement
for n in range(2, 10): # 2 to 9
  for x in range(2, n): # 
    # print('n:', n, 'x:', x)
    
    if n % x == 0:
      print(n, 'equals', x, '*', n/x)
      break
    else:
      # loop fell through without finding a factor
      print(n, 'is a prime number')

# use of continue statement
# continues with the next iteration of the loop
for num in range(2, 10):
  if num % 2 == 0:
    print('Found an even number', num)
    continue
  print('Found a number', num)