from graphics import *
import numpy

def floodfill(x, y, old, newcol):
    current=getPixel(x,y)
    if current==old :
        b=Point(xc-x,yc-y)
        b.setFill(newcol)
        b.draw(win)
        floodfill(x+1,y,old,newcol)
        floodfill(x-1,y,old,newcol)
        floodfill(x,y+1,old,newcol)
        floodfill(x,y-1,old,newcol)
        floodfill(x+1,y+1,old,newcol)
        floodfill(x-1,y+1,old,newcol)
        floodfill(x+1,y-1,old,newcol)
        floodfill(x-1,y-1,old,newcol)


def boundaryFill(x, y, fill_color, boundary_color):
    
    if(getpixel(x, y) != boundary_color & getpixel(x, y) != fill_color) :
        p=Point(x, y)
        p.setFill(fill_color)
        p.draw(win)
        boundaryFill(x + 1, y, fill_color, boundary_color)
        boundaryFill(x, y + 1, fill_color, boundary_color)
        boundaryFill(x - 1, y, fill_color, boundary_color)
        boundaryFill(x, y - 1, fill_color, boundary_color)


def main():
    win = GraphWin("Experiment 8", 1100, 600)

    # image = Image(550, 300, "image.gif")
    print("Enter 1 for floof fill and 2 for boundary fill: ")
    n=input()
    if n==1 :
        b=Rectangle(Point(50, 50), Point(150,150))
        b.setFill('black')
        b.draw(win)
        floodfill(70,70,'black','gray')
    elif n==2 :
        d=Circle(250,250,50)
        d.draw(win)
        boundaryFill(250,250,'black','gray')
    
    win.getMouse() # Pause to view result
    win.close()    # Close window when done

main()
