cards = input().split()
values = {}
for c in cards:
  rank = c[0]
  values[rank] = values.get(rank, 0) + 1
print(max(values.items(), key=(lambda key: values[key[0]]))[1])
