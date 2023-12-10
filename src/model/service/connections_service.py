from sqlite3 import Connection

class ConnectionService:
  def __init__(self, conn: Connection):
    self.conn: Connection = conn

  