import matplotlib.pyplot as plt
import csv
import time

x = []
y = []
# Draw a point based on the x, y axis value.
def draw_point(a,b):
    # Draw a point at the location (3, 9) with size 1000
    plt.scatter(a, b, s=1000)

    # Set chart title.
    plt.title("Square Numbers", fontsize=19)

    # Set x axis label.
    plt.xlabel("Number", fontsize=10)

    # Set y axis label.
    plt.ylabel("Square of Number", fontsize=10)

    # Set size of tick labels.
    plt.tick_params(axis='both', which='major', labelsize=9)

    # Display the plot in the matplotlib's viewer.
    plt.show()



with open('path.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
    	time.sleep(1)
    	draw_point(row[0],row[1])
		

