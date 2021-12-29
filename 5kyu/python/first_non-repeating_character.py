# link : https://www.codewars.com/kata/52bc74d4ac05d0945d00054e

def first_non_repeating_letter(string):
    for c in string:
        if string.upper().count(c.upper()) == 1:
            return c
    return ''

# Tests
print(first_non_repeating_letter('sTress'))