# Define a function, with keyword arguments. Another type is positional arguments. 
def my_function(a, b):
    print(f"a: {a}, b: {b}")

# Assign a variable with the name of params 
params = {'a': 1, 'b': 2, 'c': 3}

# Call the my_function by unpacking the params. 
my_function(**params)
