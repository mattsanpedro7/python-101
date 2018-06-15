width = 20
print(width)

say = 'spam eggs doesn\'t satisfy me'
sayit = '\"Yes,\" he said'

print(say, sayit)

print('C:\some\name')

#  note r before the quote
print(r'C:\some\name')

# string literals can span multiple lines
# use triple quotes
print('''\
Usage: thingy [OPTIONS]
  -h            Display this usage message
  -H hostname   Hostname to connect to
''')

# can multiply strings
print(3 * 'un' + 'ium')

# two or more string litera;s next to each other auto concatenated
# only works with two literals, not with var or expressions
print('Py' 'thon')

# to concatenate variables or variable and a literal use "+"
prefix = 'Py'
print(prefix + 'thon')

# strings can be indexed
word = 'Python'
print(word[0])

# indexes as negative numbers start counting from right
print(word[-1])

# slicing is supported
print(word[0:2])
print(word[:2])

print(word[2:])
print(word[-2:])

# python strings are immutable
# assigning to an indexed position results in err
# word[2] = 'hi'

# function len() returns length of string
print(len(word))
