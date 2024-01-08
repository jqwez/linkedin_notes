import tkinter as tk
from tkinter import ttk
from model.dao.connection_dao import ConnectionDAO


class ConnectionCard(ttk.Frame):
    def __init__(self, master=None, connection_dao=None, **kwargs):
        super().__init__(master, **kwargs)

        self.set_connection_dao(connection_dao)
        self.subtitle = f" : {self.name}"
        self.name_label = ttk.Label(self, text=self.name, padding=2)
        self.name_label.pack()
        self.company = ttk.Label(self, text=self.company, padding=2)
        self.company.pack()
        self.url_label = ttk.Label(self, text=self.url, padding=2)
        self.url_label.pack()

    def set_connection_dao(self, dao: ConnectionDAO):
        self.name = dao.name
        self.url = dao.linkedin
        self.company = dao.company
