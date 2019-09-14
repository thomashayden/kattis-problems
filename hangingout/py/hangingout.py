limit, events = map(int, input().split())
current = 0
count = 0
for i in range(events):
  event = input().split()
  people = int(event[1])
  if event[0] == "enter":
    if current + people > limit:
      count += 1
    else:
      current += people
  else:
    current -= people
print(count)
