toppings = ["pepperoni","pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]
num_two_dollar_slices = prices.count(2)
num_pizzas = len(toppings)
print("We sell", num_pizzas, "diffrent kinds of pizza!")
pizza_and_prices = [[2, "pepperoni"], [6, "pinapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]
pizza_and_prices.sort()
cheapest_pizza = pizza_and_prices[0]
priciest_pizza = pizza_and_prices[-1]
pizza_and_prices.pop(-2)
pizza_and_prices.insert(1, [2.5, "peppers"])
pizza_and_prices.sort()
three_cheapest = pizza_and_prices[0:3]
print(three_cheapest)
print(pizza_and_prices)