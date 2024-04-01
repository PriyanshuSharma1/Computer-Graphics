import math
import matplotlib.pyplot as plt

class Point :
    def __init__(self,x,y):
        self.x=x
        self.y=y

def drawLineDDA(p1,p2):

    dx= p1.x-p2.x
    dy=p1.y-p2.y

    m=dy/dx

    steps= max(abs(dx),abs(dy))

    x_inc= dx/steps
    y_inc= dy/steps

    x=p1.x
    y=p1.y

    for i in range(steps+1):
        print("({},{})".format(x,y))
        if(dx<dy):
            x=x+1
            y=y+m
        else:
            x=x+1/m
            y=y+1
        plt.plot(x, y)    # Plotting the line
        plt.show()
        

p1=Point(1,1)
p2=Point(3,3)
drawLineDDA(p1,p2)










    

   




