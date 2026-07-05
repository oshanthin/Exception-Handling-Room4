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