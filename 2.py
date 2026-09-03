sum = 0
final = 4000000
i = 1                        
def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n-1) + fib(n-2)
        
while fib(i) <= final:
    if fib(i) % 2 == 0:
        sum += fib(i)
    i += 1
   
print(sum)
