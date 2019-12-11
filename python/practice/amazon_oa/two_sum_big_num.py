# https://leetcode.com/discuss/interview-question/356960


def two_sum_big_num(array, target):
    target -= 30
    index = {}
    import sys
    max_num = -sys.maxint - 1
    result = []

    for i, num in enumerate(array):
        complement = target - num
        if complement in index:
            if max_num < max(num, complement):
                max_num = max(num, complement)
                result = [i, index[complement]]
        index[num] = i

    return sorted(result)


print two_sum_big_num([20, 50, 40, 25, 30, 10], 90)