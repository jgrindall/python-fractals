from tkinter import *

myList =[1,3,5]
myList.append(7);
myList.remove(3);
myTuple = (2, 4, 6);
for i in range(1,6):
    print(i)

def fibo(n):
    a=1;
    b=1;
    for i in range(n):
        x = a + b;
        a = b;
        b = x;
    print(x)

fibo(9);


root=Tk()
win = Canvas(root,width=1000, height=600)
win.pack()
def stopProg(e):
    root.destroy()

win.master.title("Testing...")

def cantor_set(x, y, len):
    if(len > 0.5):
        win.create_line(x, y, x + len, y)
        y = y + 40
        cantor_set(x, y, len/3)
        cantor_set(x + (2/3)*len, y, len/3)

cantor_set(50,50,800);



root.mainloop()
