from tkinter import *
 
mycolor = "white"
def paint(event):
    x1, y1 = ( event.x-3 ), ( event.y-3 )
    x2, y2 = ( event.x+3 ), ( event.y+3 )
    canvas.create_oval( x1,y1,x2,y2,fill = mycolor)
 
def change_color1():
    global mycolor
    mycolor = "red"
    
def change_color2():
    global mycolor
    mycolor = "green"
 
def change_color3():
    global mycolor
    mycolor = "yellow"
    
window = Tk()
canvas = Canvas(window)
canvas.pack()
canvas.bind("<B1-Motion>",paint)
button1 = Button(window, text="빨간색", command=change_color1)
button2 = Button(window, text="녹색", command=change_color2)
button3 = Button(window, text="노란색", command=change_color3)
 
button1.pack()
button2.pack()
button3.pack()
 
window.mainloop()