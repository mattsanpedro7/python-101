squares = [1, 4, 9, 16, 25]
print(squares)

# indexing returns item
print(squares[-1])

# splicing returns a new list
print(squares[-3:])

# lists support concatenation
print(squares + [1, 2, 3])

# lists are mutable type, unlike strings
cubes = [1, 8, 27, 65, 125]
print(cubes)
cubes[3] = 4 ** 3
print(cubes)

# add new items at end of the list by append() method
cubes.append(216)
cubes.append(7 ** 3)

print(cubes)

# array of letters, posible to replace values
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)

letters[2:5] = ['C', 'D', 'E']
print(letters);

# remove letters
letters[2:5] = []
print(letters)

# clear list by replacing elements with empty list
letters[:] = []
print(letters)

# nested lists
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0][1])
