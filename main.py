import math
import matplotlib.pyplot as plt

def solution_analytique(x):
	y = 5 * math.exp(3 * x)
	return y


start,end = 0,3
step = 0.001
number_points = int((end - start)/step)

x_values = [start]
y_values = [solution_analytique(start)]

for index_point in range(1,number_points):
	x_value = start + index_point * step
	y_value = solution_analytique(x_value)

	x_values.append(x_value)
	y_values.append(y_value)


plt.figure(figsize=(15, 6))
plt.plot(x_values, y_values)
plt.show()

