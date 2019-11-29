def digit_sum(num):
    result = 0
    while num:
        result += num % 10
        num = num // 10
    return result

def num_digit_equal_sum(nums):
    sum_to_numbers = {}
    max_equal_sum = -1
    for num in nums:
        dsum = digit_sum(num)
        if dsum in sum_to_numbers:
            other_num = sum_to_numbers[dsum]
            max_equal_sum = max(max_equal_sum, num + other_num)
            sum_to_numbers[dsum] = max(num, other_num)
        else:
            sum_to_numbers[dsum] = num
    return max_equal_sum

assert 93 == num_digit_equal_sum([60, 33, 24])
assert 84 == num_digit_equal_sum([60, 13, 24])
assert -1 == num_digit_equal_sum([51, 32, 43])

