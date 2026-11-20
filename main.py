import math
import matplotlib.pyplot as plt

def analytic_solution(x):
	y = 5 * math.exp(3 * x)
	return y

########################################################################

start, end = 0, 1
step = 0.001
number_points = int((end - start) / step)

x_values = [start]
analytic_values = [analytic_solution(start)]
approximated_values = [5]

for index_point in range(1, number_points):
	current_x_value = start + index_point * step
	current_analytic_value = analytic_solution(current_x_value)
	current_approximated_value = approximated_values[-1] * (1 + 3 * step)

	x_values.append(current_x_value)
	analytic_values.append(current_analytic_value)
	approximated_values.append(current_approximated_value)



plt.figure(figsize=(15, 6))
plt.title("Solution equation différentielle f' - 3f = 0 avec f(0)= 5")
plt.plot(x_values, analytic_values, color="blue", label="solution analytique")
plt.plot(x_values, approximated_values, color="red", marker="o", linestyle='dashed',label="solution approchée")
plt.xlabel("les valeurs de x")
plt.ylabel("les valeurs de y")
plt.legend()
plt.show()