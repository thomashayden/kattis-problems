input() # toss count
junk = list(map(int, input().split()))
min_junk = None
for i in range(len(junk)):
  if min_junk is None or junk[min_junk] > junk[i]:
    min_junk = i
print(min_junk)
