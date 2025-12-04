# link : https://www.codewars.com/kata/56b12e3ad2387de332000041

def diff(arr):
    max_diff = 0
    max_diff_str = False
    for n_couple_str in arr:
        couple_nums = n_couple_str.split('-')
        c_diff = abs(int(couple_nums[1]) - int(couple_nums[0]))
        if c_diff > max_diff:
            max_diff = c_diff
            max_diff_str = n_couple_str
     
    return max_diff_str