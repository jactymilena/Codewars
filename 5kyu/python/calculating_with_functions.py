# link : https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39
import operator

def result(number, operation):

    ops = {
        '+' : operator.add,
        '-' : operator.sub,
        'x' : operator.mul,
        '/' : operator.floordiv
    }
    return ops[operation[1]](number, operation[0])

    # Autre solution sans import
    # if operation[1] == '+':
    #     return operation[0] + number
    # elif operation[1] == '-':
    #     return number - operation[0] 
    # elif operation[1] == 'x':
    #     return operation[0] * number
    # elif operation[1] == '/':
    #     return number // operation[0]
        
def verification(value, n):
    return value if n == None else result(value, n)

def zero(n = None): return verification(0, n)
def one(n = None): return verification(1, n)
def two(n = None): return verification(2, n)
def three(n = None): return verification(3, n)
def four(n = None): return verification(4, n)
def five(n = None): return verification(5, n)
def six(n = None): return verification(6, n)
def seven(n = None): return verification(7, n)
def eight(n = None): return verification(8, n)
def nine(n = None): return verification(9, n)

def plus(n): return (n, '+') 
def minus(n): return (n, '-')
def times(n): return (n, 'x')
def divided_by(n):return (n, '/')

# Tests
print(seven(times(five())))