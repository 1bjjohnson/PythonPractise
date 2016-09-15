import calendar
from Tkinter import *

gui = Tk()
gui.title("Calendar")

def cal():
    y = 2014
    m = 4
    cal_x = calendar.month(int(y),int(m),w = 2, l = 1)
    print (cal_x)
    cal_out = Label(gui, text=cal_x, font=('courier', 12, 'bold'), bg='lightblue',justify=LEFT)
    cal_out.pack(padx=3, pady=10)

def cal2(event):
    cal_out.pack_forget(())
    y = 2014
    m = 4
    cal_x = calendar.month(int(y),int(m),w = 2, l = 1)
    print (cal_x)
    cal_out = Label(gui, text=cal_x, font=('courier', 12, 'bold'), bg='lightblue',justify=LEFT)
    cal_out.pack(padx=3, pady=10)
# cal()
gui.bind('<Return>', cal2)
button = Button(gui, text="Show",command=cal)
button.pack()

gui.mainloop()