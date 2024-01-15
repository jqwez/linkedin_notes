import tkinter as tk
from tkinter import ttk

from controller.connection_controller import ConnectionController


class AddConnectionModal(tk.Toplevel):
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master=None, *args, **kwargs)

        x, y = self.get_window_position()
        self.geometry(f"300x300+{x}+{y}")
        self.label = ttk.Label(self, text="Enter a New Connection")
        self.label.grid(column=0, row=0)
        self.cancel_button = ttk.Button(self, text="Cancel")
        self.cancel_button.bind("<Button-1>", self.handle_cancel)
        self.cancel_button.grid(column=0, row=1)
        self.submit_button = ttk.Button(self, text="Submit")
        self.submit_button.bind("<Button-1>", self.handle_submit)
        self.submit_button.grid(column=0, row=2)
        self.columnconfigure(0, weight=1)

    def handle_submit(self, event: tk.Event):
        ConnectionController.submit_new_connection(
            name="test1", url="testurl", company="testCompany"
        )

    def handle_cancel(self, event: tk.Event):
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
