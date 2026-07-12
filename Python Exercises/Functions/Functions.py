def add_list():
    all_list = []
   # Get the number of elements from the user
    n = int(input("How many elements do you want to add to the list?"))
    for i in range(n):
     user_element = int(input("Add the element:"))
      # Used .insert() to  modify all_list in place
     all_list.insert(i,user_element)
     # Return the actual list after inserting the number of elements being input by the user
    return all_list

def extract():
    return add_list()

def transform(rows):
   return [x * 2 for x in rows] # Each element from the list will be multiplied to 2

def main():
    data = transform(extract())
    print(data)

if __name__ == "__main__":
    main()

