from tkinter import *
from PIL import Image, ImageTk, ImageFilter, ImageOps
from tkinter import filedialog
from tkinter import messagebox  # Import messagebox for showing error dialogs

# Create root window
root = Tk()
root.title("Image Editor")
root.geometry("500x500")
root.configure(bg="#d1e0e0")
label1 = Label(root, text="      IMAGE EDITOR      ", font=("Ariel", 35), bg="#000000", fg="white")
label1.pack()
label2 = Label(root, text="---------------------------------------------", font=("Ariel", 25), bg="#000000", fg="white")
label2.pack()


# New window to display final image
def new(a):
    top = Toplevel(bg="#303234")
    top.title("Image Editor")
    top.geometry("1000x1000")
    b = Image.open(a)
    res = ImageTk.PhotoImage(b)
    label = Label(top, image=res)
    label.image = res
    label.pack()

# Slider function for blending    
def slider():
    global top2
    top2 = Toplevel(bg="#303234")
    top2.title("Image Editor")
    top2.geometry("1000x1000")
    global hori; global lull
    hori = Scale(top2, orient="horizontal", from_=0, to=100, command=blend1)
    hori.pack()
    default = ImageTk.PhotoImage(Image.open(f1))
    lull = Label(top2, image=default)
    lull.pack()


def blend_images(f1, f2):
    if not (f1 and f2):
        show_error_dialog("Please select two images before blending.")
    else:
        slider()

def open_image(effect):
    global f1
    if not f1:
        show_error_dialog("Please select an image.")
    else:
        if effect == 'gray':
            gray(f1)
        elif effect == 'blur':
            blur1(f1)

# Blend function
def blend1(val):

    global img
    global img2
    global i1
    global i2
    global i
    global test
    global lull
    lull.pack_forget()
    img = Image.open(f1)
    img2 = Image.open(f2)
    i2 = img2.resize((750, 750))
    i1 = img.resize((750, 750))
    i1.save(r"f1.jpg")
    i2.save(r"f2.jpg")
    i = Image.blend(i1, i2, alpha=(hori.get()) / 100)
    #change path for saving image file in required directory
    i.save(r"C:\pictures\blend1.jpg")
    test = ImageTk.PhotoImage(i)
    lull = Label(top2, image=test, pady=20)
    lull.pack()

# Grayscale function

def gray(f1):
    img = Image.open(f1)
    gr = ImageOps.grayscale(img)
    gr.save(r"C:\pictures\gr1.jpg")  # Update the path as needed
    new(r"C:\pictures\gr1.jpg")  # Open the newly saved grayscale image

    

# Blur function
def blur1(f1):
    img = Image.open(f1)
    br = img.filter(ImageFilter.BoxBlur(5))
    #change path for saving image file in required directory
    br.save(r"C:\pictures\blur1.jpg")
    new(r"C:\pictures\blur1.jpg")

# File selection dialog
def file1(button):
    button.config(state=NORMAL)
    global f1
    #change path for initial directory
    f1 = filedialog.askopenfilename(initialdir='C:\pictures', title="Select a file",
                                    filetypes=(("JPG files", "*.jpg"), ("WEBP files", "*.WebP*"), ("PNG files", "*.png")))
    e1 = Entry(top1, font=("Ariel", 12), width=100)
    e1.grid(row=1, column=2)
    e1.insert(0, f1)
    if not f1:
        show_error_dialog("Please select image ")


def file2(button):
    global f2
    #change path for initial directory
    f2 = filedialog.askopenfilename(initialdir='C:\pictures', title="Select a file",
                                    filetypes=(("JPG files", "*.jpg"), ("WEBP files", "*.webp"), ("PNG files", "*.png")))
    e2 = Entry(top1, font=("Ariel", 12), width=100)
    e2.grid(row=2, column=2)
    e2.insert(0, f2)
    if not f2:
        show_error_dialog("Please select image ")

# Opening another window for blending 
def open1():
    global f1
    global f2
    global top1
    top1 = Toplevel(bg="#d9d9d9")
    top1.title("Image Editor")
    top1.geometry("600x300")
    l1 = Label(top1, text="Select two images", font=("Berlin Sans FB", 25))
    l1.grid(row=0, column=0, sticky=N)
    l2 = Label(top1, text="Upload image 1", font=("Berlin Sans FB", 25))
    l2.grid(row=1, column=0)
    b3 = Button(top1, text='Blend', font=("Berlin Sans FB", 25), bg="#303234", fg="white", command=lambda: blend_images(f1, f2),state=DISABLED)
    b1 = Button(top1, text="Upload", font=("Berlin Sans FB", 25), bg="#303234", fg="white", command=lambda: file1(b3))
    b1.grid(row=1, column=1)
    l3 = Label(top1, text="Upload image 2", font=("Berlin Sans FB", 25))
    l3.grid(row=2, column=0)
    b2 = Button(top1, text="Upload", font=("Berlin Sans FB", 25), bg="#303234", fg="white", command=lambda: file2(b3))
    b2.grid(row=2, column=1)
    b3.grid(row=3)
    b4 = Button(top1, text='close window', font=("Berlin Sans FB", 25), bg="red", fg="white", command=top1.destroy)
    b4.grid(row=4)

# Opening another window for blurring or greyscale
def open2():
    global f1
    global top1
    top1 = Toplevel(bg="#d9d9d9")
    top1.title("Image Editor")
    top1.geometry("600x300")
    if R.get() == 2:
        l1 = Label(top1, text="Select one image", font=("Berlin Sans FB", 25))
        l1.grid(row=0, column=0, sticky=N)
        l2 = Label(top1, text="Upload image 1", font=("Berlin Sans FB", 25))
        l2.grid(row=1, column=0)
        b2 = Button(top1, text='Grayscale', font=("Berlin Sans FB", 25), bg="#303234", fg="white", command=lambda: open_image('gray'),state=DISABLED)
        b1 = Button(top1, text="Upload", font=("Berlin Sans FB", 25), bg="#303234", fg="white", command=lambda: file1(b2))
        b1.grid(row=1, column=1)
        b2.grid(row=2)
        b3 = Button(top1, text='close window', font=("Berlin Sans FB", 25), bg="red", fg="white", command=top1.destroy)
        b3.grid(row=3)
    elif R.get() == 3:
        l1 = Label(top1, text="Select one image", font=("Berlin Sans FB", 25))
        l1.grid(row=0, column=0, sticky=N)
        l2 = Label(top1, text="Upload image 1", font=("Berlin Sans FB", 25))
        l2.grid(row=1, column=0)
        b2 = Button(top1, text='Blur', font=("Berlin Sans FB", 25), bg="#303234", fg="white", command=lambda: open_image('blur'),state=DISABLED)
        b1 = Button(top1, text="Upload", font=("Berlin Sans FB", 25), bg="#303234", fg="white", command=lambda: file1(b2))
        b1.grid(row=1, column=1)
        b2.grid(row=2)
        b3 = Button(top1, text='close window', font=("Berlin Sans FB", 25), bg="red", fg="white", command=top1.destroy)
        b3.grid(row=3)

# Radiobuttons
R = IntVar()
r1 = Radiobutton(root, text="BLEND", variable=R, value=1, font=("Ariel", 30), bg="#d1e0e0", command=open1)
label3 = Label(root, text="---------------------------------------------", font=("Ariel", 25), bg="#d1e0e0",
               fg="white")
r2 = Radiobutton(root, text="GREYSCALE", variable=R, value=2, font=("Ariel", 30), bg="#d1e0e0", command=open2)
label4 = Label(root, text="---------------------------------------------", font=("Ariel", 25), bg="#d1e0e0",
               fg="white")
r3 = Radiobutton(root, text="BLUR", variable=R, value=3, font=("Ariel", 30), bg="#d1e0e0", command=open2)
label5 = Label(root, text="---------------------------------------------", font=("Ariel", 25), bg="#d1e0e0",
               fg="white")
r1.pack()
label3.pack()
r2.pack()
label4.pack()
r3.pack()
label5.pack()

# Function to display an error dialog
def show_error_dialog(message):
    messagebox.showerror("Error", message)

root.mainloop()
