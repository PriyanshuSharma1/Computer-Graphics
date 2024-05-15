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

def draw_histogram(frequencies):
    bar_width = 1
    bar_spacing = 1
    bars = []

    for i, freq in enumerate(frequencies):
        x = i * (bar_width + bar_spacing)
        p1 = Point(x, 0)
        p2 = Point(x, freq)
        bar_points = drawlineBA(p1, p2)
        bars.extend(bar_points)

    return bars

def draw_histogram(frequencies):
    bar_width = 1
    bar_spacing = 2
    bars = []

    for i, freq in enumerate(frequencies):
        x = i * (bar_width + bar_spacing)
        p1 = Point(x, 0)
        p2 = Point(x, freq)
        bar_points = drawlineBA(p1, p2)
        bars.extend(bar_points)

    return bars

def plot_histogram(frequencies, points):
    plt.figure(figsize=(10, 6))
    x_coords = [point[0] for point in points]
    y_coords = [point[1] for point in points]

    colors = plt.cm.viridis([i / len(frequencies) for i in range(len(frequencies))])
    
    for i, freq in enumerate(frequencies):
        x = i * 3
        bar_points = [(x, y) for (x, y) in zip(x_coords, y_coords) if x == i * 3]
        bar_x_coords = [p[0] for p in bar_points]
        bar_y_coords = [p[1] for p in bar_points]
        plt.scatter(bar_x_coords, bar_y_coords, color=colors[i], s=100, marker='o', label=f'Bar {i+1}')
    
    plt.grid(True)
    plt.title("Vibrant Histogram using Bresenham's Line Drawing Algorithm")
    plt.xlabel("Bar Position")
    plt.ylabel("Frequency")
    plt.legend()
    plt.show()

# Example usage
frequencies = [3, 7, 2, 5, 10]
points = draw_histogram(frequencies)
plot_histogram(frequencies, points)