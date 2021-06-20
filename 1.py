from graphics import *
def main():
    win = GraphWin("Experiment 1", 1100, 600)
    x=input("Enter value of x: ")
    y=input("Enter value of y: ")
    c = Point(x,y)
    c.draw(win)
    win.getMouse() # Pause to view result
    win.close()    # Close window when done

main()
