def drawEllipseMidpoint(rx, ry):
    # Initialize parameters
    x = 0
    y = ry
    dx = 2 * ry * ry * x
    dy = 2 * rx * rx * y

    # Region 1
    p1 = ry * ry - rx * rx * ry + 0.25 * rx * rx

    # Plot points in region 1
    while dx < dy:
        # Plot points in region 1
        plotPoint(x, y)
        
        # Move to the next point
        x += 1
        dx += 2 * ry * ry
        p1 += dx + ry * ry

        if p1 >= 0:
            y -= 1
            dy -= 2 * rx * rx
            p1 -= dy

    # Region 2
    p2 = ry * ry * (x + 0.5) * (x + 0.5) + rx * rx * (y - 1) * (y - 1) - rx * rx * ry * ry

    # Plot points in region 2
    while y >= 0:
        # Plot points in region 2
        plotPoint(x, y)
        
        # Move to the next point
        y -= 1
        dy -= 2 * rx * rx
        p2 += rx * rx - dy

        if p2 <= 0:
            x += 1
            dx += 2 * ry * ry
            p2 += dx + rx * rx

def plotPoint(x, y):
    # Print or plot the point (x, y)
    print(f"({x}, {y})")

# Define the semi-major and semi-minor axes of the ellipse
rx = 5
ry = 3

# Draw the ellipse using the Midpoint Ellipse Drawing Algorithm
drawEllipseMidpoint(rx, ry)
