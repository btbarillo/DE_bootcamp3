#Create a script. Create variables for a customer record using all four data types.

Cust_Name = str(input("Enter your name"))
Cust_Id=int(input("Enter your ID"))
Balance = float(input("Enter your balance"))
user_input = input("Is your account active [True/False]?").strip().lower()
is_active = user_input in ['true', 'yes', '1', 'y']

#Alternative way
#user_input = input("Is your account active [True/False]?")
#is_active = user_input.strip().lower() == "true"


if bool(is_active)== True:
    print(f"{Cust_Name} has a balance of {Balance}")
else:
    print(f"Your account is not active!")
