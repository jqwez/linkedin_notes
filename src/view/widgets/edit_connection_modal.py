import tkinter as tk
from tkinter import ttk

from model.dao.connection_dao import ConnectionDAO


class EditConnectionModal(tk.Toplevel):
    def __init__(self, master=None, dao: ConnectionDAO = None, *args, **kwargs):
        super().__init__(master=None, *args, **kwargs)
        self.dao = dao
        x, y = self.get_window_position()
        self.geometry(f"300x300+{x}+{y}")
        self.populate_fields()

    def populate_fields(self):
        self.action_label = ttk.Label(self, text="Edit Connection")
        self.action_label.grid(column=0, row=1)
        self.name_label = ttk.Label(self, text=self.dao.name)
        self.name_label.bind("<Button-1>", lambda event: self.handle_click_field(event))
        self.name_label.grid(column=0, row=2)
        self.cancel_button = ttk.Button(self, text="Cancel")
        self.cancel_button.bind("<Button-1>", lambda event: self.handle_cancel())
        self.cancel_button.grid(column=0, row=3)
        self.submit_button = ttk.Button(self, text="Save")
        self.submit_button.grid(column=0, row=4)
        self.columnconfigure(0, weight=1)

    def handle_cancel(self):
        self.destroy()

    def handle_click_field(self, event: tk.Event):
        widget: tk.Widget = event.widget
        content: str = widget.cget("text")
        grid_info: tk._GridInfo = widget.grid_info()
        widget.grid_forget()
        entry = tk.Entry(self, textvariable=content)
        entry.delete(0, tk.END)
        entry.insert(0, content)
        entry.grid(column=grid_info["column"], row=grid_info["row"])
        

    def get_window_position(self) -> (int, int):
        if self.master:
            window = self.master
            x = window.winfo_x()
            y = window.winfo_y()
            return (x, y)
        else:
            return (self.winfo_screenwidth() // 2, self.winfo_screenheight // 2)
