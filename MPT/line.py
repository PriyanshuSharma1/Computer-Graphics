def drawLineMidpoint(x0, y0, x1, y1):
    # Calculate differences
    dx = x1 - x0
    dy = y1 - y0

    # Initialize decision parameter and initial point
    d = dy - (dx / 2)
    x = x0
    y = y0

    # Plot initial point
    plotPoint(x, y)

    # Plot points between the two endpoints
    while x < x1:
        x += 1
        if d < 0:
            d += dy
        else:
            d += dy - dx
            y += 1
        plotPoint(x, y)

def plotPoint(x, y):
    # Print or plot the point (x, y)
    print(f"({x}, {y})")

# Define the endpoints of the line
x0, y0 = 1, 1
x1, y1 = 8, 5

# Draw the line using the Midpoint Line Drawing Algorithm
drawLineMidpoint(x0, y0, x1, y1)
