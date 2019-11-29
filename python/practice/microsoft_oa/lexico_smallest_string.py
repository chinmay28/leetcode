

def lex_smallest_string(string):
    for i in xrange(len(string) - 1):
        if string[i] > string[i+1]:
            break
    else:
        return string[:-1]

    return string[:i] + string[i+1:]

print lex_smallest_string('abczde')
print lex_smallest_string('abcdef')
print lex_smallest_string('abcrefh')
