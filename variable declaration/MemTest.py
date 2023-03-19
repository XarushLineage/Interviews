import sys

# Declare variables of different data types
num_int = 10  # Integer
num_float = 10.5  # Float
string = "Hello, world!"  # String
bool_var = True  # Boolean

# Print the size of each variable
print("Size of num_int: ", sys.getsizeof(num_int), "bytes")
print("Size of num_float: ", sys.getsizeof(num_float), "bytes")
print("Size of string: ", sys.getsizeof(string), "bytes")
print("Size of bool_var: ", sys.getsizeof(bool_var), "bytes")
