#Your Goal:
#Open a file named users.csv in Append mode. Write a string "1,Alice,Engineer\n" to it.

file_path = "C:/Users/Berna/OneDrive/Documents/CLMagno_DE_Bootcamp/Python Exercises/users.csv"

with open(file_path,"a") as f:
    f.write("1,Alice,Engineer\n")