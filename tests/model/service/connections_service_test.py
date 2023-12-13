import unittest
from sqlite3 import Connection, Cursor

from model.db.database_factory import DatabaseFactory, DatabaseFactoryEnum
from model.service.connections_service import ConnectionService
from model.dao.connection_dao import ConnectionDAO


class ConnectionServiceTest(unittest.TestCase):
    connection_service = ConnectionService(
        DatabaseFactory.new_connection(DatabaseFactoryEnum.DEV)
    )

    def setUp(self):
        DatabaseFactory.migrate(self.connection_service.conn)
        self.connection_service.save_connection("test user", "linkedin.com")

    def tearDown(self):
        conn = DatabaseFactory.new_connection(DatabaseFactoryEnum.DEV)
        cur = conn.cursor()
        cur.execute("DROP TABLE IF EXISTS connections;")
        conn.commit()

    def test_db_connection_is_valid(self):
        self.assertIsInstance(self.connection_service.conn, Connection)

    def test_saves_new_connection(self):
        connections = len(self.connection_service.get_all())
        jeremy = self.connection_service.save_connection(
            "jeremy", "linkedin.com/in/jeremyvasquez"
        )
        self.assertEqual(jeremy.name, "jeremy")
        connections2 = len(self.connection_service.get_all())
        self.assertEqual(connections + 1, connections2)

    def test_get_all(self):
        connections = self.connection_service.get_all()
        test_user: ConnectionDAO = connections[0]
        self.assertIsInstance(test_user, ConnectionDAO)
        self.assertEqual(test_user.name, "test user")

    def test_get_by_id(self):
        new_connection = self.connection_service.save_connection(
            "jeremy", "linkedin.com/in/jeremyvasquez"
        )
        fetched_connection = self.connection_service.get_by_id(new_connection.id)
        self.assertEqual(new_connection, fetched_connection)

    def test_delete_by_id(self):
        new_connection = self.connection_service.save_connection("test me", "test")
        fetched_connection = self.connection_service.get_by_id(new_connection.id)
        self.assertEqual(new_connection, fetched_connection)
        self.connection_service.delete_by_id(new_connection.id)
        fetched_connection = self.connection_service.get_by_id(new_connection.id)
        self.assertIsNone(fetched_connection)

    def test_edit_by_id(self):
        new_conneciton = self.connection_service.save_connection("test me", "test")
        self.assertEqual(new_conneciton.name, "test me")
        new_conneciton.name = "new test"
        self.connection_service.edit_by_id(new_conneciton.id, new_conneciton)
        new_version = self.connection_service.get_by_id(new_conneciton.id)
        self.assertEqual(new_conneciton, new_version)
