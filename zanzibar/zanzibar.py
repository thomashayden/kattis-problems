cases = int(input())
for i in range(cases):
  last = 1
  immigrants = 0
  sequence = list(map(int, input().split()))
  for s in sequence:
    if s == 0:
      break
    immigrants += max(0, s - (2*last))
    last = s
  print(immigrants)
