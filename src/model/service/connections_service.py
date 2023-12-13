from sqlite3 import Connection
from uuid import uuid4

from model.dao.connection_dao import ConnectionDAO

class ConnectionService:
  def __init__(self, conn: Connection):
    self.conn: Connection = conn
    self.cur = conn.cursor()
  
  def save_connection(self, name: str, url: str) -> ConnectionDAO:
    self.cur.execute("""
                INSERT INTO connections (id, full_name, linkedin)
                VALUES (?, ?, ?);
                """, (str(uuid4()), name, url))
    self.cur.execute("SELECT * FROM connections WHERE rowid=?;", 
                     (self.cur.lastrowid,))
    result = self.cur.fetchone()
    connection = ConnectionDAO.from_entry(result)
    self.conn.commit()
    return connection

  def get_all(self) -> list[ConnectionDAO]:
    self.cur.execute("SELECT * FROM connections;")
    db_entries = self.cur.fetchall()
    return [ConnectionDAO.from_entry(entry) for entry in db_entries]

  def get_by_id(self, _id: str) -> ConnectionDAO | None:
    self.cur.execute("SELECT * FROM connections WHERE id=?", (_id,))
    res = self.cur.fetchone()
    return ConnectionDAO.from_entry(res)

  def delete_by_id(self, _id: int):
    self.cur.execute("DELETE FROM connections WHERE id=?", (_id,))
    self.conn.commit()

  def edit_by_id(self, _id: int, dao: ConnectionDAO):
    self.cur.execute("UPDATE connections SET full_name=?, linkedin=? WHERE id=?;",
                     (dao.name, dao.linkedin, _id))
