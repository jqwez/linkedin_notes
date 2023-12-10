from tkinter import *
from tkinter import ttk


class MainWindow():
  root = Tk()
  frame = ttk.Frame(root, padding=10)
  frame.grid()
  ttk.Label(frame, text="hello world").grid(column=0, row=0)
  ttk.Button(frame, text="QUIT", command=root.destroy).grid(column=1, row=0)
  root.mainloop()