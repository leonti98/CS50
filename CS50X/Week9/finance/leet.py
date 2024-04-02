import math

def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0:
        return False
    numbers_list = []
    i = 0
    while x > 0:
        remainder = x % 10
        numbers_list.append(remainder)
        x = math.floor(x / 10)
    len_numbers_list = len(numbers_list)
    matches = 0
    if len_numbers_list % 2 == 0:
        my_range = round(len_numbers_list / 2)
        for i in range(my_range):
            if numbers_list[i] == numbers_list[len_numbers_list - (i + 1)]:
                matches += 1
            else:
                return False
        if matches == len_numbers_list / 2:
            return True
    else:
        my_range = round((len_numbers_list - 1)/2)
        for i in range(my_range):
            if numbers_list[i] == numbers_list[len_numbers_list - (i + 1)]:
                matches += 1
            else:
                return False
        if matches == (len_numbers_list - 1) / 2:
            return True
        
x = isPalindrome(10)
print(x)