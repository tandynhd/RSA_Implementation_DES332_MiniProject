def toBinary(a):
  l,m=[],[]
  for i in a:
    l.append(ord(i))
  for i in l:
    bins = str((bin(i)[2:]))
    m.append((bins))
  return m

print(toBinary('test'))