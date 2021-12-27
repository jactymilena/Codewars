# link : https://www.codewars.com/kata/5390bac347d09b7da40006f6

def to_jaden_case(string):
    new_string = ''
    last_c = ' '
    for c in string:
        new_string += c.upper() if last_c == ' ' else c
        last_c = c
        
    return new_string

print(to_jaden_case("how can mirrors be real if our eyes aren't real"))