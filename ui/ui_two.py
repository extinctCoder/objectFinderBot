import numpy as np
import cv2
import tkinter as tk
import PIL.Image as Image
import PIL.ImageTk as ImageTk
from image import module_img_ai
# Set up GUI
window = tk.Tk()  # Makes main window
window.wm_title("Digital Microscope")
window.config(background="#FFFFFF")

# Graphics window
imageFrame = tk.Frame(window, width=600, height=500)
imageFrame.grid(row=0, column=0, padx=10, pady=2)


def show_frame():
    cv2image = module_img_ai()
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    display1.imgtk = imgtk  # Shows frame for display 1
    display1.configure(image=imgtk)
    window.after(10, show_frame)


display1 = tk.Label(imageFrame)
display1.grid(row=1, column=0, padx=10, pady=2)  # Display 1


# Slider window (slider controls stage position)
sliderFrame = tk.Frame(window, width=600, height=100)
sliderFrame.grid(row=600, column=0, padx=10, pady=2)

show_frame()  # Display
window.mainloop()  # Starts GUI
