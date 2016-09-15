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

img = ImageTk.PhotoImage(Image.open(path))

panel = Label(root, image = img)

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
