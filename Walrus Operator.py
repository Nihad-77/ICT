# This code demostrates two exact codes that does the same thing
# After 3.8 Python update Walrus operators were introduced
# This is an example usage of it exhibiting how you can shorten your code


# Without Walrus
foods = list()
while True:
    food = input("What food do you like?: ")
    if food == "quit":
        break
    foods.append(food)
print(foods)

# With Walrus
foods = list()
while (food := input("What food do you like?: ")) != "quit":
    foods.append(food)
print(foods)

# Note: != operator has higher priority than := so parentheses here were mandatory
