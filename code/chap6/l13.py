def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(word):
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    if len(word) == 2:
        return True
    word = middle(word)
    return is_palindrome(word)

#print(middle(input()))
print(is_palindrome(input()))
