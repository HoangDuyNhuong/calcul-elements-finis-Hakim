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



'écrire fonction selon la méthode approché - éléments finis'

x_apps = [start]
y_apps = [5]
y_app = 5

number_points_app= int((end - start)/step)

for index_point_app in range (1,number_points_app):
	x_app = start + index_point_app * step
	y_app = y_app * (1 + 3 * step )

	x_apps.append(x_app)
	y_apps.append(y_app)

plt.figure(figsize=(15, 6))

plt.plot(x_values, y_values, 'b-')
plt.plot(x_apps, y_apps, 'ro')

plt.show()