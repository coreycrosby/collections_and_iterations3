#Exercise 11
one_to_onehundred = range(1,101)

for number in one_to_onehundred:
    
    if number % 3 and number % 5 == 0:
        print("BitMaker")
    
    elif number % 3 == 0:
        print("Bit")

    elif number % 5 == 0:
        print("Maker")

    else: 
        print(number)



#Exercise 12
def pizzas():
    print('How many pizzas do you want to order?')
    number_pizzas = list(range(1, (int(input())+1)))
    return number_pizzas
pizza_order = pizzas()
for pizza in pizza_order:
    print(f'How many toppings for pizza {pizza}')
    topping_number = input()
    print(f'You have ordered a pizza with {topping_number} toppings.')