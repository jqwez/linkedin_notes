import unittest
from uuid import uuid4

from model.dao.connection_dao import ConnectionDAO
from model.service.connections_service import ConnectionService
from model.db.database_factory import DatabaseFactory, DatabaseFactoryEnum


class ConnectionDAOTest(unittest.TestCase):
    conn = DatabaseFactory.new_connection(DatabaseFactoryEnum.DEV)
    DatabaseFactory.migrate(conn)
    connection_service = ConnectionService(conn)

    def test_dao_must_have_minimum_args(self):
        with self.assertRaises(TypeError):
            connection_dao = ConnectionDAO()

    def test_dao_is_created(self):
        conection_dao = ConnectionDAO(10, "jeremy", "linkedin.com/in/jeremyvasquez")
        connection_dao = ConnectionDAO(
            str(uuid4()), "jeremy", "linked.com/in/jeremyvasquez", "codingjq"
        )

    def test_dao_repr_is_produces_self(self):
        connection_dao = ConnectionDAO(
            str(uuid4()), "jeremy", "linkedin.com/in/jeremy", "codingjq"
        )
        from_repr = eval(connection_dao.__repr__())
        self.assertEqual(connection_dao, from_repr)

    def test_dao_str_is_name_and_company(self):
        connection_dao = ConnectionDAO(
            str(uuid4()), "jeremy", "linkedin.com/in/jeremy", "codingjq"
        )
        self.assertEqual(
            "Connection: jeremy, linkedin.com/in/jeremy", str(connection_dao)
        )

    def test_from_entry_returns_dao(self):
        dao_from_entry = self.connection_service.save_connection(
            "jeremy", "linkedin.com/in/jeremyvasquez"
        )
        self.assertIsInstance(dao_from_entry, ConnectionDAO)
