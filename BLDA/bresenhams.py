import math
import matplotlib.pyplot as plt

class Point:
    def __init__(self, x_coordinate,y_coordinate):
        self.x1= x_coordinate
        self.y1 = y_coordinate

def drawlineBA(p1, p2):
    ''' 
    The given function takes the two end points of the straight line and generates the points 
    in between required to plot the straight line

    Written By: Priyanshu Sharma

    '''
    #Difference between the points
    dx= p2.x1- p1.x1
    dy=p2.y1-p1.y1

    #Initial decision parameter
    Decision= 2*dy-dx

    while(p1.x1<=p2.x1):
        Point(p1.x1,p1.y1)
        print("({},{})".format(p1.x1,p1.y1))
        p1.x1+=1
        if(Decision<0):
            Decision+=2*dy
        else:
            Decision= Decision+2*dy-2*dx
            p1.y1+=1
               
p1= Point(1,1)
p2=Point(8,5)
drawlineBA(p1,p2)

    





    
    

