##Task 1: Create a variable named pi and store the value 22/7 in it. Now check the data type of this variable.

pi = 22/7
print(type(pi))


## Task 2: Below we have defined the variables for storing the principal amount, rate of interest and time. You need to calculate the simple interest for 3 years. Once simple interest is calculated, calculate the total amount you will have at the end of the tenure

principle_amount = 567.00
rate_of_interest = 5.6
time = 3

simple_interest = (principle_amount * rate_of_interest * time) /100
total_amount_including_interest = principle_amount * simple_interest
print(f"The simple interest is {simple_interest} and the total amount including the interest is {total_amount_including_interest}.")


## Task 3: There is a circular pond in a village. This pond has a radius of 84 meter. Can you find the area of the pond?

radius = 84
area_pond = 3.1416 * radius **2
print(f"The area of the pond is {area_pond}")

## Task 4: If there is a 2000 liter water in a square meter, what is the total amount of water in this pond?

## **Note:** For simplicity, use the value of pi as 3.14.

per_sqt_meter_water = 2000
total_water = area_pond * per_sqt_meter_water
print (f"The total amount of water in the pond is {total_water}")


## Task 5: If you cross a 490-meter-long street in 7 minutes, then what is your speed in meter per seconds. Print your answer with only two decimal points
## Hint: Speed = Distance / Time

distance = 490
time_speed = 7
speed = round(490/7,2)
print(f"The speed on crossing a street is {speed} meters per seconds.")

## Task 6: Create two variables to store how many fruits and vegetables you eat in a day. The value should be numeric for example 3 fruits and 4 vegetables. Now Print "You are eating x vegetables and y fruits daily" where x and y presents vegetables and fruits that you eat every day. Use python f string for this.

n_fruits = input("How many fruits do you eat daily?")
n_vegetables = input("How many vegetables do you eat daily?")

print(f"You are eating {n_vegetables} vegetables and {n_fruits} fruits daily")


## Task 7: Create a variable and store the string “The Himalayas are one of the youngest mountain range on the planet.”

## 1. Print ‘The Himalayas’ using slice operator
## 2. Print “mountain range” using negative index
## 3. Print “The Himalayas on the planet” using slice as well as f-string


the_himalayas = "The Himalayas are one of the youngest mountain range on the planet."

print(the_himalayas[0:13])
print(the_himalayas[-29:-15])
print(f"{the_himalayas[0:13]} {the_himalayas[-14:]}")

## Task 8: You have created a string variable called string= ”There are 9 planets in the solar system”. After some time, you have realized that your sentence is incorrect and there are only 8 planets, now correct your sentence by replacing the incorrect words.


planets = "There are 9 planets in the solar system"
planets = planets.replace("9","8")
print(planets)


# Task 9: Imagine you are a shop owner tracking sales of three products throughout the day. At the end of the day, you want to calculate the total sales from these products. Product quantity and prices are given below in the next code cell,

#Task: Write a program that:

#1. Calculates the total sales for each product.
#2. Summarizes the total sales for the day.
#3. Prints this summary in a formatted manner.

#Expected Output:
#Daily Sales Summary:
#- Product 1: Sold 15 units at $20.0 each, Total: $300.0
#- Product 2: Sold 10 units at $35.0 each, Total: $350.0
#- Product 3: Sold 20 units at $12.0 each, Total: $240.0
#Total Sales for the Day: $890.0

product1_quantity= 15
product1_price = 20
total_sales_product1 = product1_quantity * product1_price

product2_quantity= 10
product2_price = 35
total_sales_product2 = product2_quantity * product2_price

product3_quantity= 20
product3_price = 12
total_sales_product3 = product3_quantity * product3_price

total_sales_all_products = total_sales_product1 + total_sales_product2 + total_sales_product3

print("Daily Sales Summary:")
print(f"- Product 1: Sold {product1_quantity} units at ${product1_price} each, Total: ${total_sales_product1}")
print(f"- Product 2: Sold {product2_quantity} units at ${product2_price} each, Total: ${total_sales_product2}")
print(f"- Product 3: Sold {product3_quantity} units at ${product3_price} each, Total: ${total_sales_product3}")
print(f"Total Sales for the Day: ${total_sales_all_products}")


