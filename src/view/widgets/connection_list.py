import tkinter as tk
from tkinter import ttk

from model.dao.connection_dao import ConnectionDAO
from view.widgets.edit_connection_modal import EditConnectionModal

dummy_connections = [ConnectionDAO(i, "jere ", "url") for i in range(0, 10)]


class ConnectionListWidget(ttk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.button = ttk.Button(
            self,
            text="Get Connections",
            command=lambda: self.update_data(dummy_connections),
        ).grid(column=0, row=0, columnspan=2, sticky="nsew")

    def update_data(self, data):
        self.connection_row(is_header=True, column=0, row=1)
        for i, connection in enumerate(data):
            self.connection_row(dao=connection, column=0, row=i + 2)

    def connection_row(
        self, dao: ConnectionDAO = None, is_header=False, column: int = 0, row: int = 0
    ):
        if is_header == True:
            name = ttk.Label(master=self, text=f"Name")
            name.grid(column=column, row=row)
            url = ttk.Label(master=self, text=f"LinkedIn")
            url.grid(column=column + 1, row=row)
        else:
            name = ttk.Label(master=self, text=f"{dao.name}")
            name.grid(column=column, row=row)
            url = ttk.Label(master=self, text=f"{dao.linkedin}")
            url.grid(column=column + 1, row=row)
            edit = ttk.Label(master=self, text="⛭")
            edit.bind("<Button-1>", lambda _: self.edit_connection(dao))
            edit.grid(column=column + 2, row=row)

    def edit_connection(self, dao: ConnectionDAO):
        modal = EditConnectionModal(self)
