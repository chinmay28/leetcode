

def get_optimal_pairs(alist, blist, target):
    alist.sort(key=lambda x: x[1])
    blist.sort(key=lambda x: x[1])
    # we pick smaller number from a and bigger number from b
    i = 0
    j = len(blist) - 1

    pair_list = []
    import sys
    max_sum = -sys.maxint - 1

    while i < len(alist) and j >= 0:
        test_sum = alist[i][1] + blist[j][1]

        if test_sum > target:
            j -= 1  # sum too big, let's pick a smaller number from blist
            continue

        if max_sum < test_sum:
            # we have new max sum
            pair_list = []
            max_sum = test_sum

        if max_sum <= test_sum:
            pair_list.append([alist[i][0], blist[j][0]])
            # we also need to add all duplicates on the blist end
            k = j - 1
            while k >= 0 and blist[k][1] == blist[k+1][1]:
                pair_list.append([alist[i][0], blist[k][0]])
                k -= 1
        i += 1

    return pair_list


if __name__ == "__main__":
    a = [(1,3), (2,5), (3,7), (4,10)]
    b = [(1,2), (2,3), (3,4), (4,5)]
    print get_optimal_pairs(a, b, 10)
