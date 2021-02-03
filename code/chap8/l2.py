fruit = "apple"
index = 0
while index < len(fruit):
    print(fruit[index])
    index += 1

for c in fruit:
    print(c)

prefixes = 'JKLMNOPQ'
suffix = 'ack'

for l in prefixes:
    print(l + suffix)

print(fruit[:3])
print(fruit[3:])
print(fruit[1:3])
print(fruit[:])
newf = "p" + fruit[1:]
print(newf)

# linear search
def find(word, letter, index=0):
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
    return -1

print(find("Sakura", "k"))
print(find("Sakura", "f"))
print(find("Sakura", "k", 3))
