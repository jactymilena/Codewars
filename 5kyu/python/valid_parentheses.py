def valid_parentheses(string):
    sum = 0 
    for c in string:
        if c == '(':
            sum += 1 
        elif c == ')':
            sum -= 1
            if sum < 0:
                return False
    return sum == 0

# Tests
print(valid_parentheses("  ("))
print(valid_parentheses(")test"))
print(valid_parentheses("()()"))