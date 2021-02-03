poem = '''Ther was a young lady named Bright,
Whose speed was far faster than light;
She started one day
In a relative way,
And returned on the privious night.
加藤'''

print(len(poem))

fout = open('relativity.txt', 'wt', encoding='utf-8')
fout.write(poem)
fout.close()

fout_print = open('relativity_print.txt', 'wt', encoding='utf-8')
print(poem, file=fout_print)
fout.close()

# Write file by list
fout3 = open('relativity_chunk.txt', 'wt', encoding='utf-8')
size = len(poem)
offset = 0
chunk = 100
while True:
  if offset > size:
    break
  fout3.write(poem[offset:offset+chunk])
  offset += chunk
fout.close()

print('after wring relativity.txt')

try:
  fout4 = open('relativity.txt', 'xt')
  fout4.write('stomp stomp stomp')
except FileExistsError:
  print('relativity.txt already exits!. That was a close one')
