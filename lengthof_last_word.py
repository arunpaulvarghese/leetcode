# length of last word in a given word string
def lengthoflast(word):
    length = 0
    i = len(word) - 1
    while i >=0 and word[i] == ' ':
        i -= 1
    while i>=0 and word[i] != ' ':
        length +=1
        i-= 1
    return length

w = "hai there how are you"
print(lengthoflast(w))
