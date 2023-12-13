import tkinter as tk
from tkinter import ttk
from model.dao.connection_dao import ConnectionDAO

dummy_connections = [ConnectionDAO(i, "jere ", "url") for i in range(0, 10)]


class ConnectionListWidget(ttk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.button = ttk.Button(
            self, text="update", command=lambda: self.update_data(dummy_connections)
        ).grid(column=0, row=0)
        self.label = ttk.Label(self, text="Connection Name").grid(column=0, row=1)
        self.label2 = ttk.Label(self, text="LinkedIn Url").grid(column=1, row=1)
        self.number = 0

    def update_data(self, data):
        self.number += 1
        for i, connection in enumerate(data):
            self.label = ttk.Label(
                self, text=f"{connection.name}" + str(self.number)
            ).grid(column=0, row=i + 2)
            self.label2 = ttk.Label(self, text=f"{connection.linkedin}").grid(
                column=1, row=i + 2
            )
