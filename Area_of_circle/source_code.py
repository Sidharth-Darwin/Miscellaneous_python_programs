import numpy as np
from math import pi
import matplotlib.pyplot as plt

rad = float(input("Enter the radius of circle: "))
no_of_units = float(input("Enter the value of dr: "))
no_of_area_units = int(rad/no_of_units)

array_x=np.array([])
array_y=np.array([])
list_dr=np.linspace(0.0,rad,num=no_of_area_units ,endpoint=True)
for dr in list_dr:
    # radius of each small rectangles that is used to find the area
    width = np.array([dr])
    height = np.array([2*pi*dr])
    array_x = np.append(array_x,width)
    array_y = np.append(array_y,height)

# plotting the bar graph to show the area of the circle  
plt.bar(array_x, array_y, facecolor='g',width=no_of_units)
plt.xlabel('Radius r')
plt.ylabel('Circumference 2πr (width of rectangle)')
plt.title('Area of Circle')
plt.grid(True)
plt.show()

# area of all the rectangles in the graph is aprox equal to area of the circle 
Area_vector = array_y*no_of_units
print("area using graph",sum(Area_vector))
# area of the triangle in the graph is aprox equal to the area of the circle
# area of triangle = (1/2)*b*h = (1/2)*r*2πr = πr**2
# thats how area of circle formula is formed 
print("area using formula", pi*(rad**2))

