#Dtaypes and Variables in Python

#Data types in Python 

# **int**: Integer, a whole number without a decimal point (e.g., 5, -3).
int = 10

# **float**: Floating-point number, a number that has a decimal point (e.g., 3.14, -0.001).    
float = 3.14

# **complex**: Complex numbers, which have a real and an imaginary part (e.g., 2 + 3j).
complex = 2 + 3

# **str**: String, a sequence of characters enclosed in quotes (e.g., "Hello", 'Python').
str = "Hello, World!"

# **bool**: Boolean, a type that can be either True or False.
bool = True

# **list**: A collection of items that can be of different types, ordered and changeable (e.g., [1, 2, 3], ["apple", "banana"]).
list = [1, 2, 3, "apple", "banana"]

# **tuple**: Similar to a list, but immutable (cannot be changed after creation) (e.g., (1, 2, 3), ("apple", "banana")).
tuple = (1, 2, 3, "apple", "banana")

# **set**: An unordered collection of unique items (e.g., {1, 2, 3}, {"apple", "banana"}).
set = {1, 2, 3, "apple", "banana"}

# **dict**: Dictionary, a collection of key-value pairs (e.g., {"name": "Alice", "age": 30}).
dict = {"name": "Alice", "age": 30, "is_student": False}


# Variable Naming Rules

#1. Magaca variable-ka waa inuu ku bilaabmaa xaraf (a-z, A-Z) ama hoos-xariiq (_)

    #✅ name = "Ali"
    #❌ 1name = "Ali" (lama oggola)

#2. Variable-yadu waa case-sensitive
    # Tusaale: myVariable iyo MyVariable waa laba magac oo kala duwan.

#3.Magaca variable-ka ma noqon karo keyword (eray ka tirsan Python)

    #Tusaale: lama isticmaali karo if, while, else iwm.

#4.Isticmaal magacyo macno leh oo sharaxaya waxa variable-ku qabanayo

   #✅ age = 25 (macne leh)
   #❌ x = 25 (ma caddeynayo waxa la kaydiyay)

#5. Isticmaal hoos-xariiq (snake_case) si loo kala saaro ereyada

   #✅ user_name = "Ali"
   #❌ usernameandage = "Ali25"


#Variables in Python
# Create variable
Name = "Mohamed Dahir"
Age = 10
MyGPA = 3.0
# Print variable
print("Name:", Name)
print("Age:", Age)
print("My GPA:", MyGPA) 

# Variable Types
int_variable = 42          # Integer
float_variable = 3.14     # Float
str_variable = "Hello"    # String
# Boolean variable
bool_variable = True       # Boolean   
# Print variable types
print("Integer Variable:", int_variable)
print("Float Variable:", float_variable)
print("String Variable:", str_variable)
print("Boolean Variable:", bool_variable)


#1. Numeric data types
# Numeric data types in Python include integers, floats, and complex numbers.
# Integers are whole numbers, floats are decimal numbers, and complex numbers have a real and imaginary part.
# Example of numeric data types
int_num = 10              # Integer (tiro dhan)
float_num = 3.14         # Float (tiro jajab leh)
complex_num = 2 + 3j     # Complex number (tiro isku dhafan)

#2. Strings
# Strings are sequences of characters enclosed in quotes. They can be single (' '), double (" "), or triple (''' ''' or """ """) quoted.
# Strings can contain letters, numbers, and special characters.
str_single = 'Hello'      # Single-quoted string
str_double = "World"      # Double-quoted string
str_triple = """This is a multi-line string."""  # Triple-quoted string
#3. Boolean
# Boolean data types represent truth values: True or False.
bool_true = True          # Boolean True
bool_false = False        # Boolean False
#4. Lists
# Lists are ordered collections of items that can be of different data types. They are mutable, meaning you can change their content.
list_example = [1, 2, 3, "apple", "banana"]  # List containing integers and strings
#5. Tuples
# Tuples are similar to lists but are immutable, meaning their content cannot be changed after creation
tuple_example = (1, 2, 3, "apple", "banana")  # Tuple containing integers and strings
#6. Sets
# Sets are unordered collections of unique items. They do not allow duplicate values.
set_example = {1, 2, 3, "apple", "banana"}  # Set containing integers and strings
#7. Dictionaries
# Dictionaries are collections of key-value pairs. Each key is unique, and you can access values using their keys.
dict_example = {"name": "Alice", "age": 30, "is_student": False}  # Dictionary with string keys and mixed values

