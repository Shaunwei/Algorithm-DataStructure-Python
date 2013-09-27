#Fill a 1-D array with random values, then
#print them, one per line
from array import array
import random

#generate len array
def Array(len):
	a = [0]*100
	return array('f',a)

#the constructor is called to create the array
valueList = Array(100)

#Fill the array with random floating-point values
for i in range(len(valueList)):
	valueList[i] = random.random()

#print the values, one per line.
for value in valueList:
	print(value)

