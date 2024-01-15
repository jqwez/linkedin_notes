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
        self.name_label = self.editable(text=self.dao.name, row=2) 
        self.url_label = self.editable(text=self.dao.linkedin, row=3)
        self.columnconfigure(0, weight=1)

    def editable(self, text: str, row: int = 0) -> ttk.Label:
        label: ttk.Label = ttk.Label(self, text=text)
        label.bind("<Button-1>", self.handle_click_field)
        label.grid(column=0, row=row)
        return label
        
    def handle_cancel(self, event: tk.Event):
        self.destroy()

    def handle_click_field(self, event: tk.Event):
        widget: tk.Widget = event.widget
        content: str = widget.cget("text")
        grid_info: tk._GridInfo = widget.grid_info()
        widget.grid_forget()
        widget.destroy()
        entry = ttk.Entry(self, textvariable=content)
        entry.bind("<Return>", self.handle_accept_entry)
        entry.bind("<FocusOut>", self.handle_accept_entry)
        entry.delete(0, tk.END)
        entry.insert(0, content)
        entry.grid(column=grid_info["column"], row=grid_info["row"])

    def handle_accept_entry(self, event: tk.Event):
        widget: tk.Widget = event.widget
        content: str = widget.get()
        grid_info: tk._GridInfo = widget.grid_info()
        widget.grid_forget()
        widget.destroy()
        label = ttk.Label(self, text=content)
        label.bind("<Button-1>", self.handle_cancel)
        label.grid(column=grid_info["column"], row=grid_info["row"])

    def get_window_position(self) -> (int, int):
        if self.master:
            window = self.master
            x = window.winfo_x()
            y = window.winfo_y()
            return (x, y)
        else:
            return (self.winfo_screenwidth() // 2, self.winfo_screenheight // 2)
