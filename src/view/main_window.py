import tkinter as tk
from tkinter import ttk
from view.widgets.connection_list import ConnectionListWidget


class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("800x800")
        self.title("Networking Notes")
        self.views: dict[str : tk.Frame | ttk.Frame] = {}

        self.add_view("connection_list", ConnectionListWidget)
        self.transition_view("connection_list")

    @property
    def view(self):
        return self.views.get("current")

    @view.setter
    def view(self, frame: tk.Frame | ttk.Frame):
        self.views["current"] = frame

    def add_view(self, view_name: str, view_frame: tk.Frame, *args, **kwargs):
        if type(view_name) != str:
            raise TypeError("Not a valid string")
        if not issubclass(view_frame, (tk.Frame, ttk.Frame)):
            raise TypeError("Not a valid tk.Frame object")
        self.views[view_name] = view_frame(self, *args, **kwargs)

    def transition_view(self, next_view_name):
        if self.view:
            self.view.pack_forget()

        next_view = self.views.get(next_view_name)
        if next_view:
            next_view.pack(fill=tk.BOTH, expand=True)
            self.view = next_view
