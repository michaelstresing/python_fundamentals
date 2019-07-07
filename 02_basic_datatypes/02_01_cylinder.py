'''
Write the necessary code calculate the volume and surface area
of a cylinder with a radius of 3.14 and a height of 5. Print out the result.


'''

#needed for pi
import math

#cylinder dimensions
r = 3.14
h = 5

#volume
v = math.pi * r ** 2 * 5
print(v)

#surface area
sa = 2 * math.pi * r * h + 2 * math.pi * r ** 2
print(sa)
