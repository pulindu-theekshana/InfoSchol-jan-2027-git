# num = 1

# while num <= 10:
#     print("*"*num)
#     num += 1

# num = 10

# while num >= 1:
#     print("*"*num)
#     num -= 1

num = 1
space = 5

while num <= 10:
    print(" "*space, end="*"*num)
    num += 2
    space -= 1
    print("\n")