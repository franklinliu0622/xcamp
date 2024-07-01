def get_ones(num):
    ones_digit = num % 10
    return ones_digit 

test_num = int(input('Enter:'))
result = get_ones(test_num)
print(result)