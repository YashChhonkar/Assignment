n = 5  

print("Lower Triangular Pattern:")
for i in range(1, n + 1):
    print("* " * i)
print() 

print("Upper Triangular Pattern:")
for i in range(n):
    print("  " * i + "* " * (n - i))
print()

print("Pyramid Pattern:")
for i in range(n):
    spaces = "  " * (n - i - 1)
    stars = "* " * (2 * i + 1)
    print(spaces + stars)
