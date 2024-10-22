# Longest substring without repeating the characters
def longest_substring(stri):
    sceen = {}
    l = 0
    length = 0
    for r in range(len(stri)):
        char = stri[r]
        if char in sceen and sceen[char] >= l:
            l = sceen[char] + 1
        else:
            length = max(length, r-l+1)
        sceen[char] = r
    return length


st = "abcdcbdd"
print(longest_substring(st))
