#random generator
import random
import my_moduleForDay4
random_integer =random.randint(1,10)
print(random_integer)
print(my_moduleForDay4.pi)
#floating point from  0 to 1.0 exclusive
random_float=random.random()

print(random_float)

#to exapnd the range of floating point as it does not take any arguments
#random_float*5
#0.0000... - 4.99999...
random_float=random.random()*5
print(random_float)
