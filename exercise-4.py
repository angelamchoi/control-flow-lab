# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

triangle_a = input(
"""Enter the three lengths of a triangle (one at a time): 
a:""").lower()

triangle_b = input(
"""Enter the three lengths of a triangle (one at a time): 
b:""").lower()

triangle_c = input(
"""Enter the three lengths of a triangle (one at a time): 
c:""").lower()

if triangle_a == triangle_b == triangle_c:
  print(f"A triangle with sides of {triangle_a}, {triangle_b}, and {triangle_c} is an equilateral triangle.")

if triangle_a != triangle_b != triangle_c:
  print(f"A triangle with sides of {triangle_a}, {triangle_b}, and {triangle_c} is a scalene triangle.")

if triangle_a == triangle_b or triangle_b == triangle_c or triangle_c == triangle_a:
  print(f"A triangle with sides of {triangle_a}, {triangle_b}, and {triangle_c} is an isosceles triangle.")

#### NOTES ####
# use multi-line comment