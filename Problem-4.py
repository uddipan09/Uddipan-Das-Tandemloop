input_list = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]

# Initialize an empty dictionary
count_dict = {}

# Loop from 1 to 9
for i in range(1, 10):
    count_dict[i] = 0  # Set each key to 0

# Count multiples
for num in input_list:
    for i in range(1, 10):
        if num % i == 0:
            count_dict[i] += 1

print(count_dict)
