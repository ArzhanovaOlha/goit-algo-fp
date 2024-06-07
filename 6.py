items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}
budget = 100


def greedy_algorithm(items, budget):
  items_sorted = sorted(items.items(), key = lambda x: x[1]['calories'] / x[1]['cost'], reverse = True)

  total_calories = 0
  remaining_budget = budget
  chosen_items =[]

  for item, details in items_sorted:
    if details['cost'] <= remaining_budget:
      chosen_items.append(item)
      remaining_budget -= details['cost']
      total_calories += details['calories']

  return total_calories, remaining_budget, chosen_items

find_greedy = greedy_algorithm(items, budget)
print('Greedy algorithm result',find_greedy)

def dynamic_programming(items, budget):
    dp = [0] * (budget + 1)
    item_selection = [[] for _ in range(budget + 1)]

    for item_name, item in items.items():
        cost = item["cost"]
        calories = item["calories"]

        for current_budget in range(budget, cost - 1, -1):
            if dp[current_budget - cost] + calories > dp[current_budget]:
                dp[current_budget] = dp[current_budget - cost] + calories
                item_selection[current_budget] = item_selection[current_budget - cost] + [item_name]

    max_calories = max(dp)
    max_calories_budget = dp.index(max_calories)
    selected_items = item_selection[max_calories_budget]

    return max_calories, budget - max_calories_budget, selected_items

find_dynamic = dynamic_programming(items, budget)
print('Dynamic programming result', find_dynamic)