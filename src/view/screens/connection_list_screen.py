import tkinter as tk
from tkinter import ttk

from view.widgets.connection_list import ConnectionListWidget

class ConnectionListScreen(ttk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        self.subtitle = f" : Connections"

        self.connection_list = ConnectionListWidget()
        self.connection_list.pack()

