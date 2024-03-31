#include <iostream>
#include <cmath>
using namespace std;

// Structure to represent a point (x,y)
struct Point
{
    int x, y;
};

void drawLineDDA(Point p1, Point p2){
    //Calculating the differences
    int dx= p1.x - p2.x;
    int dy = p1.y- p2.y;

    //Slope Calculation
    int m= round(dy/dx);



    //Calculating the steps
    int steps = max(abs(dx),abs(dy));

    // //Calculating increments for x and y coordinates
    // float x_inc= float(dx)/steps;
    // float y_inc= float(dy)/steps;

    //Initialize the current position as the starting point
    float x = p1.x;
    float y= p1.y;

    //Points on the line
    for(int i =0; i<= steps; i++){
        cout<<"("<<round(x)<<","<<round(y)<<")"<<endl;
        if(dx>=dy){
            x=x+1;
            y=y+m;
        }
        else{
            x=x+1/m;
            y=y+1;
        }
    }
}

int main(){
    Point p1={1,1};
    Point p2={3,3};
    drawLineDDA(p1,p2);

}