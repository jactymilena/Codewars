# link : https://www.codewars.com/kata/5dd462a573ee6d0014ce715b

def same_case(a, b): 
    if not (a.isalpha() and b.isalpha()):
        return -1
    if (a.isupper() and b.isupper()) or (not a.isupper() and not b.isupper()):
        return 1
    return 0