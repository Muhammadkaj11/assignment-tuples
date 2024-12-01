def calculate_product(tup):
    product = 1  
    for number in tup:
        product *= number
    return product

numbers_tuple = (2, 3, 4, 5)
result = calculate_product(numbers_tuple)
print("The product of all numbers in the tuple is:", result)
