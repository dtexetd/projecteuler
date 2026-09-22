num = 2
i = 0
while i != 10001:
  prime = True
  for j in range(2, num):
    if (num%j==0):
      prime = False
  if prime:
    i += 1
    print(i, num)
  num += 1