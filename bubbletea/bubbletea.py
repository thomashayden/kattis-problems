import math

input() # flush the number of kinds of teas
tea_costs = list(map(int, input().split()))
input() # flush the number of kinds of toppings
topping_costs = list(map(int, input().split()))
lookup = {}
for i in range(len(tea_costs)):
  combos = list(map(int, input().split()))
  lookup[i] = combos[1:]

# Now look through all of the options and see which one is cheapest
cheapest = None
for i in range(len(tea_costs)):
  for topping_num in lookup[i]:
    cost = tea_costs[i] + topping_costs[topping_num - 1]
    if cheapest is None or cheapest > cost:
      cheapest = cost

# Now calculate how many cups can be bought for the given amount of money
money = int(input())
cups = max(1, math.floor(money / cheapest))
print(cups - 1)
