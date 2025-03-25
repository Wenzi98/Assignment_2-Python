
my_list = []

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

my_list.insert(1, 15)

# Add more numbers to the list
my_list.extend([50, 60, 70])

# Remove the last item
my_list.pop()


my_list.sort()

# Find and print the index of 30
print("Final list:", my_list)
print("Index of 30:", my_list.index(30))