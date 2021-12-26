# link : https://www.codewars.com/kata/52597aa56021e91c93000cb0

def move_zeros(array):
  if 0 not in array:
    return array
  new_array = []
  for number in array: # insertion de tous les chiffres sauf zeros
    if number != 0:
      new_array.append(number)
  if len(new_array) < len(array): 
    for i in range(len(new_array), len(array)): # insertion des zeros a la fin
      new_array.append(0)
        
    return new_array

# Test
array = [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9, 0, 0, 5, 6, 0, 0, 8, 9, 0]
print(move_zeros(array))
