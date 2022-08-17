"""
Classes are a way to organize data and functionality together, wa can add more organization to our
code with something called a module
"""
import math, statistics # we import class math
print("The value of pi is") 
print(math.pi) # we call class math and variable pi

scores = [4, 2, 5, 2, 1]
mean = statistics.mean(scores)
print(f'Mean score is {mean}')

'''
we can use the keyboard (from) to extract only functions we care about
'''
from math import pi 
print(f"value of is {pi}")

'''
if stumle with variable that have same name we can rename or change name class or function
'''

import math as mtk  # like this 
print(mtk.pi)

from math import pi as lingkaran
print(f"rumus lingkaran adalah {lingkaran}")
