def rotate_word(word, loop):
    res = ""
    loop = loop % (ord("z") - ord("a"))
    for c in word:
        newc = ord(c) + loop
        if newc > ord("z"):
            newc -= (ord("z") - ord("a"))
        res += chr(newc)
    return res

print(rotate_word("word", 43))
