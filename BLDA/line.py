import matplotlib.pyplot as plt

class Point:
    def __init__(self, x_coordinate, y_coordinate):
        self.x1 = x_coordinate
        self.y1 = y_coordinate

def drawlineBA(p1, p2):
    ''' 
    The given function takes the two end points of the straight line and generates the points 
    in between required to plot the straight line.
    '''
    points = []
    
    x1, y1 = p1.x1, p1.y1
    x2, y2 = p2.x1, p2.y1

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1

    if dx > dy:
        err = dx / 2.0
        while x1 != x2:
            points.append((x1, y1))
            err -= dy
            if err < 0:
                y1 += sy
                err += dx
            x1 += sx
        points.append((x2, y2))
    else:
        err = dy / 2.0
        while y1 != y2:
            points.append((x1, y1))
            err -= dx
            if err < 0:
                x1 += sx
                err += dy
            y1 += sy
        points.append((x2, y2))

    return points

def plot_lines(lines):
    plt.figure(figsize=(10, 6))
    
    for line in lines:
        points = drawlineBA(line[0], line[1])
        x_coords = [point[0] for point in points]
        y_coords = [point[1] for point in points]
        plt.plot(x_coords, y_coords, marker='o', label=f'Line {line[2]}')
    
    plt.grid(True)
    plt.title("Lines using Bresenham's Line Drawing Algorithm")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.show()

# Example lines with different slopes
lines = [
    (Point(1, 1), Point(8, 5), 'Line 1 (|m| < 1)'),
    (Point(1, 1), Point(5, 8), 'Line 2 (|m| >= 1)')
]

plot_lines(lines)
