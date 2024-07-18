import tkinter as tk
from PIL import Image, ImageTk

def open_image_fullscreen(image_path):
    # Create the root window
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.bind('<Escape>', lambda e: root.destroy())

    # Open the image file
    img = Image.open(image_path)
    img = ImageTk.PhotoImage(img)

    # Create a label to display the image
    label = tk.Label(root, image=img)
    label.pack(expand=True)

    # Start the Tkinter main loop
    root.mainloop()

if __name__ == "__main__":
    image_path = 'C:/repos/SDDanielson_KeyboardScripts/Scripts/Button1/pic.jpg'
    open_image_fullscreen(image_path)
