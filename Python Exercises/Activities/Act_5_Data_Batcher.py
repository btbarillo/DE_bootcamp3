#Goal: Use a for loop to print out a status message for 10 files.

num = ["Jan.csv", "Feb.csv", "March.csv", "April.csv", "May.csv", "June.csv", "July.csv", "August.csv", "September.csv", "October.csv", "November.csv", "December.csv"]

for i in range(len(num)):
    print(f"Processing file {num[i]}....")