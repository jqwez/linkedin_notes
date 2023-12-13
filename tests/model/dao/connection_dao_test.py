import unittest

from model.dao.connection_dao import ConnectionDAO
from model.service.connections_service import ConnectionService
from model.db.database_factory import DatabaseFactory, DatabaseFactoryEnum


class ConnectionDAOTest(unittest.TestCase):
    connection_service = ConnectionService(
        DatabaseFactory.new_connection(DatabaseFactoryEnum.DEV)
    )

    def test_dao_must_have_minimum_args(self):
        with self.assertRaises(TypeError):
            connection_dao = ConnectionDAO()

    def test_dao_is_created(self):
        conection_dao = ConnectionDAO(10, "jeremy", "linkedin.com/in/jeremy")

    def test_from_entry_returns_dao(self):
        return
        self.connection_service.new_connection(
            "jeremy", "linkedin.com/in/jeremyvasquez"
        )
