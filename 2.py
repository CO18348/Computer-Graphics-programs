from graphics import *
def main():
    win = GraphWin("Experiment 2", 1100, 600)
    x = 20
    y = 20
    b=Point(x,y)
    x1=50
    y1=50
    x2=50
    y2=500
    c = Line(Point(x1,y1),Point(x2,y2))
    b.draw(win)
    c.draw(win)
    s = (y2 - y1) * x + (x1 - x2) * y + (x2 * y1 - x1 * y2)
    if y1==y2 :
        if s<0 :
            msg=Text(Point(500,400), 'The point lies below the line')
            msg.draw(win)
        elif s>0 :
            msg=Text(Point(500,400), 'The point lies above the line')
            msg.draw(win)
        elif s==0 :
            msg=Text(Point(500,400), 'The point lies on the line')
            msg.draw(win)
    elif x1==x2 :
        if s<0 :
            msg=Text(Point(500,400), 'The point lies on the left of the line')
            msg.draw(win)
        elif s>0 :
            msg=Text(Point(500,400), 'The point lies on the right side of the line')
            msg.draw(win)
        elif s==0 :
            msg=Text(Point(500,400), 'The point lies on the line')
            msg.draw(win)
    elif (y2-y1)<(x2-x1) :
        if s < 0 :
            msg=Text(Point(500,400), 'The point lies below the line or left side of the line')
            msg.draw(win)
        elif s > 0 :
            msg=Text(Point(500,400), 'The point lies above the line or right side of the line')
            msg.draw(win)
        else :
            msg=Text(Point(500,400), 'The point lies on the line')
            msg.draw(win)
    elif (y2-y1)>(x2-x1) :
        if s < 0 :
            msg=Text(Point(500,400), 'The point lies below the line or left side of the line')
            msg.draw(win)
        elif s > 0 :
            msg=Text(Point(500,400), 'The point lies above the line or right side of the line')
            msg.draw(win)
        else :
            msg=Text(Point(500,400), 'The point lies on the line')
            msg.draw(win)
    
    
    win.getMouse() # Pause to view result
    win.close()    # Close window when done

main()
