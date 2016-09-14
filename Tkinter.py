from Tkinter import *
from tkFileDialog import *
from PIL import ImageTk, Image

root = Tk()
root.wm_title("META tool")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
# root.overrideredirect(1)
root.geometry("%dx%d+0+0" % (w, h))
# root.geometry("880x370+100+100")
# root.configure(background='grey')

path = "photo.jpg"

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))
#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = Label(root, image = img)

#The Pack geometry manager packs widgets in rows or columns.
panel.pack(side = "top", fill = "both", expand = "yes")

# top = Toplevel()
# top.withdraw()
# root.withdraw()
fileName = askopenfilename()

if len(fileName) <= 0:
    # Label(root, text="No File Selected").pack()
    print "No file selectd"
elif len(fileName) > 0:
    # root.destroy()
    print (fileName)
