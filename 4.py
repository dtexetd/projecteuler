def Solution():
    largest = 0
    for i in range(999,99,-1):
        for j in range(i, 99, -1):
            product = i * j
            if product > largest and str(product) == str(product)[::-1]:
                largest = product
    return largest
            
print(Solution())