weight = 20


#ground shipping
if weight <= 2:
    ground_cost = weight * 1.5 + 50
elif weight <= 6:
    ground_cost = weight * 3 + 20
elif weight <= 10:
    ground_cost = weight * 4 + 20
else:
    ground_cost = weight * 4.75 + 20

print("the cost of ground is $" , ground_cost)

cost_ground_premium = "125.00"
print("the cost of ground premium is $" +cost_ground_premium)
#drone shipping

if weight <= 2:
    drone_cost = weight * 4.5
elif weight <= 6:
    drone_cost = weight * 9
elif weight <= 10:
    drone_cost = weight * 12
else:
    drone_cost = weight * 14

print("the cost of drone is $" , drone_cost)