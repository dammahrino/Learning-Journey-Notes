# Arguments, kwargs (keyword arguments)

# Function with positional arguments
def user_info(name, age, city):
    """This function prints name, age, and city from
    an argument provided to the function

    Args:
        name (String): Name of the person
        age (int): Age in years
        city (String): City where you live
    """
    print("{} is {} years old, from {}.".format(name, age, city))
    
user_info("Daniel", 30, "Mexico City")

# Keyword arguments
def user_info2(name, age = 0, city = "Mexico City"):
    print("{} is {} years old, from {}.".format(name, age, city))
    
user_info2("Alberto")
user_info2(age = 44, name = "Gabriel")

# *args and **args
# *args:
#     Allows for unlimited variables to be passed into a function without defining them ahead of time

# **kwargs
#     Allows for unlimited keyword arguments to be passed into a function without defining them ahead of time
# def application(**kwargs):
#     print(**kwargs)
#     
# application(name = "Daniel", email = "my_email@someplace.com")
# application(name = "Alberto", last_name = "Cadena", age = 24)

# All three types of arguments can be used in a single function BUT in order (args -> *args -> **kwargs)
def some_function(fname, lname, email, company, *args, **kwargs):
    print("{} {} works at {}. The email is {}.".format(fname, lname, company, email))
    print(args)
    print(kwargs)
    
some_function("Daniel", "Cadena", "some_email@email.mx", "Tech Company", 6500, hire_date = "2022/09/15")