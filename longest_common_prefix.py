# longest common prefix
def longestCommonPrefix(prefix):
    if len(prefix) == 0:
        return ""
    base = prefix[0]
    for i in range(len(prefix)):
        for word in prefix[1:]:
            if word[i] != base[i] or i == len(word):
                return base[0:i]
    return base


pre = ["flower","flow","flight"]
print(longestCommonPrefix(pre))
