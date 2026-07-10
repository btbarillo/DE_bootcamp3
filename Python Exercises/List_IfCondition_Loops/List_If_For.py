### Task 1: 1. You are a Marvel fan and created a list of superheroes.
##avengers  = [‘Iron Man’, ‘Captain America’, ‘Black Widow’, ‘Hulk’, ‘Thor’, ‘Hawkeye’]
##Using this list, calculate how many members in the Avengers team?


avengers= ["Iron Man", "Captain America", "Black Widow", "Hulk", "Thor", "Hawkeye"]
print(len(avengers))


### Task 2 Awesome. Now Iron Man made Spider-Man a new member of the Avengers, add him to your list at the end

avengers.append("Spider-Man")
print(avengers)


### Task 3
### Looks like you are loving this avengers exercise already😄, Let's add a twist to it. Everyone came to a conclusion that Captain America is the leader of the Avengers, so please add him before the Iron Man. Hint: You can first remove him from the list and add before the Iron Man. To remove him you can use a method called .pop()
###💡 Feel free to take help of ChatGPT just in case you are confused about pop() method. Remember becoming a good Python programmer is all about how well you can learn new things on your own

avengers.pop(1)
avengers.insert(0, "Captain America")
print(avengers)


### Task 4
## Thor and Hulk are getting angry easily and fight with each other. So you have to separate them with each other. To separate them, move “Black Widow” in between them.

avengers.pop(2)
avengers.insert(3, "Black Widow")
print(avengers)


### Task 5
### Below list contains scores of students in a class as per their roll number. Which means the first element is for roll # 1, second one is for roll # 2 and so on. Print the scores of,
## 1. The first student
## 2. The last student
## 3. First 3 students
## 4. Scores of roll # 3, 4 and 5

scores = [92, 85, 76, 58, 89, 91, 73, 84]

print(scores[0])
print(scores[-1])
print(scores[:3])
print(scores[2:5])



### Task 6 We got a result of one more student which is 83 marks. 
## Append this to the scores at the end and print the list


scores.append(83)
print(scores)


### Task 7 Categorizes each score into a grade based on the following thresholds:

#1. A: 90 to 100
#1. B: 80 to 89
#1. C: 70 to 79
#1. D: 60 to 69
#1. F: Below 60

# Count the number of students in each grade category and print the summary of how many students received each grade. 

#Expected output
#Grade Summary:
#- A: 2 students
#- B: 4 students
#- C: 2 students
#- D: 0 students
#- F: 1 students

scores = [92, 85, 76, 58, 89, 91, 73, 84]
grade_A = grade_B = grade_C = grade_D = grade_F = 0

for score in scores:
    if score >= 90:
        grade_A += 1
    elif score >= 80:
        grade_B += 1
    elif score >= 70:
        grade_C += 1
    elif score >= 60:
        grade_D += 1
    else:
        grade_F+=1


print(f"Grade Summary:")
print(f"A: {grade_A} students")
print(f"B: {grade_B} students")
print(f"C: {grade_C} students")
print(f"D: {grade_D} students")
print(f"F: {grade_F} students")

## Alternative code

scores = [92, 85, 76, 58, 89, 91, 73, 84]

# Initialize dictionary to store counts
grade_counts = {
    'A': 0,
    'B': 0,
    'C': 0,
    'D': 0,
    'F': 0
}

# Categorize and count each score
for score in scores:
    if score >= 90:
        grade_counts['A'] += 1
    elif score >= 80:
        grade_counts['B'] += 1
    elif score >= 70:
        grade_counts['C'] += 1
    elif score >= 60:
        grade_counts['D'] += 1
    else:
        grade_counts['F'] += 1

# Print the summary
print("Grade Summary:")
for grade, count in grade_counts.items():
    print(f"- {grade}: {count} students")



### Task 8 Managing inventory efficiently is crucial for businesses to ensure they do not run out of key products. This exercise simulates a simple inventory management system where the user can see which items are below the minimum stock level and need reordering. Below you have two lists that stores product names and their inventory stock levels.Using that,

##1. Check each item to see if its stock level is below a minimum threshold.
##1. If the stock level is below the minimum, add the product's name to a reorder list.
##1. Print a list of products that need to be reordered.

##Expected Output
##Items to Reorder:
#- Pears
#- Grapes


# Lists to store product names and stock levels
product_names = ["Apples", "Bananas", "Oranges", "Pears", "Grapes"]
stock_levels = [20, 50, 15, 5, 8]

minimum_stock = 10  # Minimum stock before reordering


reorder_list =[]

for i in range(len(product_names)):
    if stock_levels[i] < 10:
        reorder_list.append(product_names[i])

print(f"Items to Reorder:")
for product in reorder_list:
    print(f"-{product}")