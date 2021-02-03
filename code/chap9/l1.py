def has_no_e(word):
    return not('e' in word)

def avoids(word, c):
    return not(c in word)

def update_list(word, char_list):
    for c in word:
        char_list[ord(c) - ord("a")][1] += 1
    return char_list

def uses_only(word, chars):
    for c in word:
        if c in chars:
            continue
        return False
    return True

def uses_all(word, chars):
    return uses_only(chars, word)

def is_abecedarian(word):
    wl = list(word)
    wl.sort()
    sorted_word = "".join(wl)
    if word == sorted_word:
        return True
    return False

def is_that(word):
    f = 0
    i = 0
    while i < len(word) - 1:
        if word[i] == word[i + 1]:
            f += 1
            i += 2
            if f == 3:
                return True
            continue
        f = 0
        i += 1
    return False

def main1():
    c = input()
    all_count = 0
    noe_count = 0
    char_list = [[i + ord("a"), 0] for i in range(26)]
    f = open('words.txt', 'r')
    for line in f:
        all_count += 1
        word = line.strip()
        char_list = update_list(word, char_list)
        if avoids(word, c):
            noe_count += 1
            print(word)
    f.close()
    pas = int(noe_count / all_count * 100)
    print(pas)
    char_list = sorted(char_list, key=lambda x : x[1])
    for i in range(5):
        print(chr(char_list[i][0]))

def main2():
    c = input()
    f = open('words.txt', 'r')
    for line in f:
        word = line.strip()
        if uses_only(word, c):
            print(word)
    f.close()

def main3():
    c = input()
    count = 0
    f = open('words.txt', 'r')
    for line in f:
        word = line.strip()
        if uses_all(word, c):
            print(word)
            count += 1
    print(count)
    f.close()

def main4():
    count = 0
    with open('words.txt', 'r') as f:
        for line in f:
            word = line.strip()
            if is_abecedarian(word):
                print(word)
                count += 1
    print(count)

def main5():
    with open('words.txt', 'r') as f:
        for line in f:
            word = line.strip()
            if is_that(word):
                print(word)


if __name__ == "__main__":
    main5()
