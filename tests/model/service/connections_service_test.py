import unittest
from sqlite3 import Connection, Cursor

from model.db.database_factory import DatabaseFactory, DatabaseFactoryEnum
from model.service.connections_service import ConnectionService

class ConnectionServiceTest(unittest.TestCase):
  connection_service = ConnectionService(
    DatabaseFactory.new_connection(DatabaseFactoryEnum.DEV)
  )
  
  def test_db_connection_is_valid(self):
    self.assertIsInstance(self.connection_service.conn, Connection)

    
