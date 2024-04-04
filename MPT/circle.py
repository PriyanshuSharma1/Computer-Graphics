import matplotlib.pyplot as plt

def drawCircleMidpoint(radius):
    x = 0
    y = radius
    d = 1 - radius  # Initial decision parameter

    # List to store the coordinates of points on the circle
    circle_points = []

    while y >= x:
        # Plot points in all octants
        circle_points.append((x, y))
        circle_points.append((y, x))
        circle_points.append((-x, y))
        circle_points.append((-y, x))
        circle_points.append((-x, -y))
        circle_points.append((-y, -x))
        circle_points.append((x, -y))
        circle_points.append((y, -x))

        if d <= 0:
            d += 2 * x + 3
        else:
            d += 2 * (x - y) + 5
            y -= 1
        x += 1

    return circle_points

# Define the radius of the circle
radius = 5

# Get the points on the circle using midpoint circle algorithm
circle_points = drawCircleMidpoint(radius)

# Extract x and y coordinates from the list of points
x_values, y_values = zip(*circle_points)

# Plot the circle
plt.scatter(x_values, y_values)
plt.gca().set_aspect('equal', adjustable='box')
plt.title('Midpoint Circle Drawing Algorithm')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()