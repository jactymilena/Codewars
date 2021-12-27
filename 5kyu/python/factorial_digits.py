# link : https://www.codewars.com/kata/58fea5baf3dff03a6e000102

import math
       
def factor_digit(n):
    if n == 0:
        return 1
    digits = 0
    for i in range(2 ,n + 1):
        digits += math.log10(i)

    return math.floor(digits) + 1

# Test
print(factor_digit(10))