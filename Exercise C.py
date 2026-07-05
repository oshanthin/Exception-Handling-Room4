#AttributeError
#text = "Hello World"
#print(text.append("!"))

'''
try:
    text = "Hello World"
    text.append("!")
except AttributeError:
    print("You tried to use a method that doesn't exist for this object.")
'''
#ImportError / ModuleNotFoundError
'''
import maths
print(math.sqrt(16))
'''


'''
try:
    import math
except ModuleNotFoundError:
    print("Module not found. Check spelling or install it.")
print(math.sqrt(16))
'''
#RECURSIONERROR
'''
def recurse():
    return recurse()

recurse()
'''

'''
def recurse(n):
    if n == 0:
        return "Done"
    return recurse(n - 1)

print(recurse(5))
'''

'''
try:
    def recurse():
        return recurse()
    recurse()
except RecursionError:
    print("Too many recursive calls!")
'''