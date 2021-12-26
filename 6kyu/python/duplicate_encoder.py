# link : https://www.codewars.com/kata/54b42f9314d9229fd6000d9c

def duplicate_encode(word):
    new_word = ''
    word = word.lower()
    for charac in word:
      nb_occurences = word.count(charac)
      new_word += ')' if(nb_occurences > 1) else '('
  
    return new_word

# Test
print('Success')
print(duplicate_encode('Success'));