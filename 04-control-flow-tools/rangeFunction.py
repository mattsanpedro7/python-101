for i in range(5):
  print(i)
  
for i in range(11, 19):
  print(i)

# a step with range
print(range(10, -100, -30))

# iterate over indices of a sequence
# combine range() and len()
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
  print(i, a[i])

# behaves as a list but it isn't
# it doesn't make the list
print(range(10))
print(range(0, 10))

# function list() creates lists from iterables
myList = list(range(5,11))
print(myList)
