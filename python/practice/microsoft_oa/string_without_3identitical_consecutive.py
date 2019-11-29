
def string_without_3conseq(string):
    result = string[:1]
    count = 1

    for i in xrange(1, len(string)):
        if string[i] == string[i-1]:
            count += 1
        else:
            count = 1

        if count < 3:
            result += string[i]

    return result

print string_without_3conseq("eedaaad")
print string_without_3conseq("xxxtxxx")
print string_without_3conseq("uuuuxaaaaxuuu")
