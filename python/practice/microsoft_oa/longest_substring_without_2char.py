

def longest_substring(string):
    result = ""
    i = 0
    if string.find('aaa') == -1 and string.find('bbb') == -1:
        return string

    while i < len(string):
        apos = string.find('aaa', i)
        bpos = string.find('bbb', i)

        if apos == -1 and bpos == -1:
            result = max(result, string[i:], key=len)
            break

        if apos == -1:
            result = max(result, string[i:bpos+2], key=len)
            i = bpos + 1
        elif bpos == -1:
            result = max(result, string[i:apos + 2], key=len)
            i = apos + 1
        else:
            result = max(result, string[i:min(apos, bpos) + 2], key=len)
            i = min(apos, bpos) + 1

    return result


print longest_substring("aabbaaaaabb")
print longest_substring("aabbaabbaabbaa")





