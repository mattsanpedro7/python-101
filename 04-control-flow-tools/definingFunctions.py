# def fib(n):
#   a, b = 0, 1
#   while a < n:
#     print(a, end=',')
#     a, b = b, a+b
#   print()

# fib(2000)
# f = fib
# f(100)


# print(fib(0)) # none

# default argument values
def ask_ok(prompt, retries=4, reminder='Please try again!'):
  while True:
    ok = input(prompt)
    # in keyword tests whether or not sequence contains certain value
    if ok in ('y', 'ye', 'yes'):
      return True
    if ok in ('n', 'no', 'nop', 'nope'):
      return False
    retries = retries - 1
    if retries < 0:
      raise ValueError('invalid user response')
    print(reminder)

# ask_ok('OK to overwrite the file? ', 2, 'Come on, only yes or no!')

# default values at point of function in the defining scope
i = 5

def g(arg=i):
  print(arg)

i = 6
g()

# this function accumulates arguments
def f(a, L=[]):
  L.append(a)
  return L

print(f(1))
print(f(2))
print(f(3))

# if you don't want to share function between subsequent calls
def h(a, L=None):
  if L is None:
    L = []
  L.append(a)
  return L

print(h(1))
print(h(2))
print(h(3))

