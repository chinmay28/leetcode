def min_count(string):
    acount = string.count('a')
    bcount = string.count('b')
    small_count = bcount if acount > bcount else acount
    if not any(['aaa' in string, 'bbb' in string]):
        return 0
    if small_count == 0:
        return 0
    if small_count > 8:
        return (n-8)/2 + 3
    if small_count <= 4 > 0:
        return 1
    if small_count > 4 <=8:
        return 2

assert 1 == min_count('baaaaa')
assert 2 == min_count('baabbaabbba')
assert 0 == min_count('baabab')

