import tkinter as tk

root = tk.Tk()
root.title("Hello GUI World")
root.geometry("400x300") # W * H PIXEL

label = tk.Label(root, text="Hello World", font=("Arial",16))
label.pack(pady=20)

root.mainloop()




