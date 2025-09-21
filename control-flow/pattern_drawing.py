# pattern_drawing.py

# Step 1: Prompt user for input
size = int(input("Enter the size of the pattern: "))

# Step 2: Draw square pattern using while + for
row = 0
while row < size:
    for col in range(size):
        print("*", end="")  # print stars without new line
    print()  # move to next line after each row
    row += 1
