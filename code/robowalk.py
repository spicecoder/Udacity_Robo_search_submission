
# Import pyplot module and alias it as plt. This can avoid repeatly call pyplot.
import matplotlib.pyplot as plt

# Draw a point based on the x, y axis value.
def draw_point():
    # Draw a point at the location (3, 9) with size 1000
    plt.scatter(3, 9, s=1000)

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

draw_point()