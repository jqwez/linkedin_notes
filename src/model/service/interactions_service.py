from sqlite3 import Connection
from datetime import datetime
from uuid import uuid4

from model.dao.interaction_dao import InteractionDAO


class InteractionService:
    def __init__(self, conn: Connection):
        self.conn: Connection = conn
        self.cur = conn.cursor()

    def save_interaction(
        self, connection_id: str, notes: str, date_interaction: datetime
    ):
        self.cur.execute(
            """
          INSERT INTO interactions (id, connection_id, notes, date_created, date_interaction)
          VALUES (?, ?, ?, ?, ?);
                     """,
            (str(uuid4()), connection_id, notes, datetime.now(), date_interaction),
        )
        self.cur.execute(
            "SELECT * FROM interactions WHERE rowid=?;", (self.cur.lastrowid,)
        )
        result = self.cur.fetchone()
        interaction = InteractionDAO.from_entry(result)
        self.conn.commit()
        return interaction

    def get_all(self) -> list[InteractionDAO]:
        self.cur.execute("SELECT * FROM interactions;")
        results = [InteractionDAO.from_entry(result) for result in self.cur.fetchall()]
        return results

    def get_by_id(self, _id: str) -> InteractionDAO | None:
        self.cur.execute("SELECT * FROM interactions WHERE id=?", (_id,))
        result = self.cur.fetchone()
        return InteractionDAO.from_entry(result)

    def delete_by_id(self, _id: str):
        self.cur.execute("DELETE FROM interactions WHERE id=?", (_id,))
        self.conn.commit()

    def edit_by_id(self, _id: str, dao: InteractionDAO):
        self.cur.execute(
            "UPDATE interactions SET connection_id=?, notes=?, date_interaction=? WHERE id=?",
            (dao.connection_id, dao.notes, dao.date_interaction, _id),
        )
