# link : https://www.codewars.com/kata/56a1c074f87bc2201200002e

def smaller(arr):
    small_array = []
    for i in range(len(arr)) :
        small_array.append(0)
        for j in range(i + 1, len(arr)):
            if(arr[i] > arr[j]):
                small_array[i] += 1

    return small_array

# Tests
print(smaller([5, 4, 3, 2, 1]))
print(smaller([1, 2, 3]))
