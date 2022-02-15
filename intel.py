num1 = 42 #variable declaration, initialize integer
num2 = 2.3 #variable declaration, initialize floating-point
boolean = True # variable declaration,initialize boolean
string = 'Hello World'#variable declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}#variable declaration, initialize dictionary, boolean
fruit = ('blueberry', 'strawberry', 'banana')#variable declaration, initialize tuple
print(type(fruit)) #function, typecheck, tuple
print(pizza_toppings[1]) #function,list, list[1]
pizza_toppings.append('Mushrooms')
print(person['name'])#log statement
person['name'] = 'George' #function , dicitonary,access value
person['eye_color'] = 'blue'#variable declaration
print(fruit[2])#log,statement

if num1 > 45:
    print("It's greater")
else:
    print("It's lower")#conditionals, log statement

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")#conditionals, log statement

for x in range(5):#for loop, log statement
    print(x)
for x in range(2,5):#for loop, log statement
    print(x)
for x in range(2,10,3):#for loop, log statement
    print(x)
x = 0
while(x < 5):#while loop, log statement
    print(x)
    x += 1

pizza_toppings.pop()#variable, pop same as push
pizza_toppings.pop(1)# variable, pop same as push with value

print(person)# log statement
person.pop('eye_color')
print(person)

for topping in pizza_toppings:#for loop, conditional statement ,log statement
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times(): #function, parameter
    for num in range(10):
        print('Hello')# log statement

print_hello_ten_times()#fucntion argument

def print_hello_x_times(x):#function, parameter argument, log statement
    for num in range(x):#for loop
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10)::#function, parameter argument, log statement
    for num in range(x):# for loop
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)