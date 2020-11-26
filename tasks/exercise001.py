# In this Kata, you will be given an array of numbers in which two numbers occur once and
# the rest occur only twice.
# Your task will be to return the sum of the numbers that occur only once.
# For example, repeats([4,5,7,5,4,8]) = 15 because only the numbers 7 and 8 occur once,
# and their sum is 15.
# More examples in the test cases below.

# Good luck!
'''
assert repeats([4,5,7,5,4,8]) == 15
assert repeats([9, 10, 19, 13, 19, 13]) == 19
assert repeats([16, 0, 11, 4, 8, 16, 0, 11]) == 12
assert repeats([5, 17, 18, 11, 13, 18, 11, 13]) == 22
assert repeats([5, 10, 19, 13, 10, 13]) == 24
'''

def repeats(arr):
    test = int(input('Enter number between 1-5: '))
    if test == 1:
        arr = [4,5,7,5,4,8]
    elif test == 2:
        arr = [9, 10, 19, 13, 19, 13]
    elif test == 3:
        arr = [16, 0, 11, 4, 8, 16, 0, 11]
    elif test == 4:
        arr = [5, 17, 18, 11, 13, 18, 11, 13]
    elif test == 5:
        arr = [5, 10, 19, 13, 10, 13]
    else:
        print('You entered out of range')

    total = 0

    for num in arr:
        if arr.count(num) == 1:
            total += num

    return f'{arr} == {total}'

print(repeats(arr=input('Press enter')))
