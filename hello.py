# hello.py

def divide(a, b):
    return a / b        # BUG: division by zero possible

def list_access():
    numbers = [1, 2, 3]
    return numbers[10] # BUG: index out of range

def undefined_usage():
    print(user_name)   # BUG: undefined variable

divide(10, 0)
list_access()
undefined_usage()
