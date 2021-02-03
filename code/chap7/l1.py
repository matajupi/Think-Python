def countdown(n):
    while n > 0:
        print(n)
        n -= 1
    print("Blastoff")

#countdown(10)
while True:
    query = input("> ")
    if query == "done":
        break

print("Done")
