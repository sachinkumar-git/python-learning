# Write a program that takes a list of numbers and removes all duplicates using a set.

# Sample list with duplicates
numbers = [10, 20, 10, 30, 40, 20, 50, 40]

# Converting list to set (removes duplicates) and back to list
unique_numbers = list(set(numbers))

print(f"Original List: {numbers}")
print(f"List after removing duplicates: {unique_numbers}")




# Given a dictionary of products and their prices, find the product with the highest price.
products = {
    "Laptop": 45000,
    "Smartphone": 25000,
    "Headphones": 2500,
    "Smartwatch": 5000
}

# Finding the key with the maximum value
highest_product = max(products, key=products.get)
highest_price = products[highest_product]

print(f"Product with highest price: {highest_product} (₹{highest_price})")



#Write a program that merges two dictionaries into one.

dict_a = {"name": "Sachin", "branch": "AI/ML"}
dict_b = {"college": "SRM University AP", "cgpa": 8.78}

# Method 1: Using | operator (Python 3.9+)
merged_dict = dict_a | dict_b

# Method 2: Using unpacking (Works in older versions too)
# merged_dict = {**dict_a, **dict_b}

print(f"Merged Dictionary: {merged_dict}")