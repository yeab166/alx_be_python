# multiplication_table.py

# Step 1: Prompt user for input
number = int(input("Enter a number to see its multiplication table: "))

# Step 2: Generate and print multiplication table (1 to 10)
for i in range(1, 11):
    product = number * i
    print(f"{number} * {i} = {product}")
