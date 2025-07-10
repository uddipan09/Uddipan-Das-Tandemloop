a = int(input("Enter a number: "))

# If even, reduce by 1
if a % 2 == 0:
    a = a-1

for i in range(1, a + 1):
    print(2 * i - 1, end=", " if i < a else "\n")
