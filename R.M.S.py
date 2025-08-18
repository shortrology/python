#Restaurant Management System
#This program allows users to order items from a restaurant menu and calculates the total order amount.

#Define the menu of restaurant
menu = {
    "burger": 100,
    "pizza": 900,
    "pasta": 400,
    "salad": 300,
    "sada": 350,
    "coffee":50,
}
print("Welcome to the restarant")
print("Pizza:Rs.900\nPasta:Rs.400\nSalad:Rs.300\nSada:Rs.350\nBurger:Rs.100\nCoffee.Rs.50")

#take the order from user

order_total = 0
item_1 = input("Enter the name of item you want to order:")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order:")
else:
    print(f"Ordered item {item_1} is not available in the menu")

another_order = input("Do you want to order another item? (yes/no): ")
if another_order == "yes":
    item_2 = input("Enter the name of item you want to order:")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your item {item_2} has been added to your order:")
    else:
        print(f"Order item {item_2} is not available in the menu")
    print("Your total order amount is:", order_total)
else:
    print("Thank you for visiting our restaurant!")
    