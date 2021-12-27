# link : https://www.codewars.com/kata/520b9d2ad5c005041100000f

def pig_it(text):
    new_text = ''
    for word in text.split():
        new_text += word[1:] + word[0] + 'ay ' if word != '?' and word != '!' else word + ' '
    return new_text[0:-1]

# Test
print(pig_it('Pig latin is cool ?'))