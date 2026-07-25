#Your Goal:
#Open a file named users.csv in Append mode. Write a string "1,Alice,Engineer\n" to it.


with open("users.csv","a") as f:
    f.write("1,Alice,Engineer\n")