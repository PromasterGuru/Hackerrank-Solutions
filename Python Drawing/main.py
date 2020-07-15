import random
# Variables
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
drawings = ['_','*']

for i in range(rows):
    for j in range(cols):
        index = random.randint(0,1)
        print(drawings[index], end="")
    print("\n")
