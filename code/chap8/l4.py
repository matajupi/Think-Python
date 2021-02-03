def in_both(word1, word2):
    s = ""
    for l in word1:
        if l in word2:
            s += l
    return s

print(in_both("hhana", "wnakkja"))
print("asas" > "nesnes")
print("nesasane" > "kosuke")
