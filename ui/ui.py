from tkinter import *
from hand_ui import get_hand_ui
from robot_ui import get_robot_ui
from image import module_img_ai
import numpy as np
import cv2
import tkinter as tk
import PIL.Image as Image
import PIL.ImageTk as ImageTk

root = Tk()
root.title('Object Detection Robot')
handFrame = get_hand_ui(root)
robotFrame = get_robot_ui(root)
handFrame.grid(row=1, column=0, sticky='EW')
robotFrame.grid(row=0, column=0, sticky='EW')
imageFrame = Frame(root, width=600, height=500)
imageFrame.grid(row=0, column=1, rowspan=2)


def show_frame():
    cv2image = module_img_ai()
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    display1.imgtk = imgtk
    display1.configure(image=imgtk)
    root.after(1, show_frame)


display1 = tk.Label(imageFrame)
display1.grid(row=0, column=1, rowspan=2) 

show_frame()
root.mainloop()
