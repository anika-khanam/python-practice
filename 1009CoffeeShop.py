# Module 1 Self-Assessment: Coffee Shop
size_cost = {"small": 2, "medium": 3, "large": 4}
coffee_cost = {"brewed": 0, "espresso": 0.50, "cold brew": 1}
flavor_cost = {"none": 0, "hazelnut": 0.50, "vanilla": 0.50, "caramel": 0.50}

print("Welcome to the coffee shop!")
print("--------------------")
print("Here is our menu:")
print("Sizes")
print("--------------------")
print("small: $2, medium: $3, large: $4")
print("--------------------")
print("Type")
print("--------------------")
print("brewed: no additional cost, espresso: 50 cents, cold brew: $1")
print("--------------------")
print("Flavoring")
print("--------------------")
print("None: no additional cost, All other options: 50 cents")
print("--------------------")

size = input("Do you want a small, medium, or large coffee?: ").lower()
coffee_type = input("Do you want brewed, espresso, or cold brew?: ").lower()
syrupchoice = input("Do you want a flavored syrup? (Yes or No): ").lower()

if syrupchoice == 'yes':
    flavor = input("Do you want hazelnut, vanilla, or caramel?: ").lower()
else:
    flavor = "none"

size_price = size_cost.get(size, 0)
coffee_price = coffee_cost.get(coffee_type, 0)
flavor_price = flavor_cost.get(flavor, 0)

total_cost = size_price + coffee_price + flavor_price
tip = total_cost * 0.15
total_cost_with_tip = total_cost + tip

if flavor == "none":
    summary_message = f"You asked for a {size} cup of {coffee_type} coffee with no flavoring."
else:
    summary_message = f"You asked for a {size} cup of {coffee_type} coffee with {flavor} syrup."

print(f"\n{summary_message}")
print(f"Your cup of coffee costs ${total_cost:.2f}")
print(f"The price with a tip is ${total_cost_with_tip:.2f}")
