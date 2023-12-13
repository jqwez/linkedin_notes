import unittest
from sqlite3 import Connection, Cursor
from uuid import uuid4
from datetime import datetime

from model.db.database_factory import DatabaseFactory, DatabaseFactoryEnum
from model.service.connections_service import ConnectionService
from model.service.interactions_service import InteractionService
from model.dao.interaction_dao import InteractionDAO


class InteractionServiceTest(unittest.TestCase):
    interaction_service = InteractionService(
        DatabaseFactory.new_connection(DatabaseFactoryEnum.DEV)
    )
    connection_service = ConnectionService(interaction_service.conn)

    def setUp(self):
        DatabaseFactory.migrate(self.interaction_service.conn)
        test_interaction = self.interaction_service.save_interaction(
            str(uuid4()), "test notes", datetime.now()
        )

    def tearDown(self):
        conn = DatabaseFactory.new_connection(DatabaseFactoryEnum.DEV)
        cur = conn.cursor()
        cur.execute("DROP TABLE IF EXISTS interactions;")
        conn.commit()

    def test_db_interaction_is_valid(self):
        self.assertIsInstance(self.interaction_service.conn, Connection)

    def test_saves_new_interaction(self):
        interactions = len(self.interaction_service.get_all())
        test_interaction = self.interaction_service.save_interaction(
            str(uuid4()), "notes", datetime.now()
        )
        self.assertEqual(test_interaction.notes, "notes")
        interactions2 = len(self.interaction_service.get_all())
        self.assertEqual(interactions + 1, interactions2)

    def test_get_all(self):
        interactions = self.interaction_service.get_all()
        test_user: InteractionDAO = interactions[0]
        self.assertIsInstance(test_user, InteractionDAO)
        self.assertEqual(test_user.notes, "test notes")

    def test_get_by_id(self):
        new_interaction = self.interaction_service.save_interaction(
            str(uuid4()), "notes", datetime.now()
        )
        fetched_interaction = self.interaction_service.get_by_id(new_interaction.id)
        self.assertEqual(new_interaction, fetched_interaction)

    def test_delete_by_id(self):
        new_interaction = self.interaction_service.save_interaction(
            str(uuid4()), "notes", datetime.now()
        )
        fetched_interaction = self.interaction_service.get_by_id(new_interaction.id)
        self.assertEqual(new_interaction, fetched_interaction)
        self.interaction_service.delete_by_id(new_interaction.id)
        fetched_interaction = self.interaction_service.get_by_id(new_interaction.id)
        self.assertIsNone(fetched_interaction)

    def test_edit_by_id(self):
        new_interaction = self.interaction_service.save_interaction(
            str(uuid4()), "notes", datetime.now()
        )
        self.assertEqual(new_interaction.notes, "notes")
        new_interaction.notes = "new test"
        self.interaction_service.edit_by_id(new_interaction.id, new_interaction)
        new_version = self.interaction_service.get_by_id(new_interaction.id)
        self.assertEqual(new_interaction, new_version)
