import tkinter as tk
from tkinter import ttk

from model.dao.connection_dao import ConnectionDAO


class EditConnectionModal(tk.Toplevel):
    def __init__(self, master=None, dao:ConnectionDAO=None, *args, **kwargs):
        super().__init__(master=None, *args, **kwargs)
        self.dao = dao
        x, y = self.get_window_position()
        self.geometry(f"300x300+{x}+{y}")
        self.populate_fields()
        

    def populate_fields(self):
      self.action_label = ttk.Label(self, text="Edit Connection")
      self.action_label.pack()
      self.cancel_button = ttk.Button(self, text="Cancel")
      self.cancel_button.bind("<Button-1>", lambda event: self.handle_cancel())
      self.cancel_button.pack()
      self.submit_button = ttk.Button(self, text="Save")
      self.submit_button.pack()

    def handle_cancel(self):
        self.destroy()

    def get_window_position(self) -> (int, int):
        if self.master:
            window = self.master
            x = window.winfo_x()
            y = window.winfo_y()
            return (x, y)
        else:
            return (self.winfo_screenwidth()//2, self.winfo_screenheight//2)
