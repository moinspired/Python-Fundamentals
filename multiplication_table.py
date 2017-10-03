import sys
product = ""
for row in range(1, 12):
    for col in range(1, 12):
        product += str(row * col) + " "
print product
