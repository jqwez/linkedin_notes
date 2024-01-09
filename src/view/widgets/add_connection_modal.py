import tkinter as tk
from tkinter import ttk


class AddConnectionModal(tk.Toplevel):
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master=None, *args, **kwargs)

        x, y = self.get_window_position()
        self.geometry(f"300x300+{x}+{y}")
        self.label = ttk.Label(self, text="Enter a New Connection").grid(
            column=0, row=0
        )
        self.cancel_button = ttk.Button(self, text="Cancel")
        self.cancel_button.bind("<Button-1>", lambda event: self.handle_cancel())
        self.cancel_button.grid(column=0, row=1)
        self.submit_button = ttk.Button(self, text="Submit").grid(column=1, row=1)

    def handle_cancel(self):
        self.destroy()

    def get_window_position(self) -> (int, int):
        if self.master:
            window = self.master
            x = window.winfo_x()
            y = window.winfo_y()
            print(x, y)
            return (x, y)
        else:
            return (self.winfo_screenwidth() // 2, self.winfo_screenheight // 2)
