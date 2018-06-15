words = ['a', 'bird', 'cat']
for w in words:
  print(w, len(w))

# mod a seq
# loop over a slice copy of the entire list
for w in words[:]:
  if len(w) > 1:
    words.insert(0, w)

print(words)
