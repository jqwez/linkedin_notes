import unittest
from sqlite3 import Connection, Cursor

from model.db.database_factory import DatabaseFactory, DatabaseFactoryEnum

class DatabaseFactoryTest(unittest.TestCase):
  
  def test_connects_to_production_database(self):
    connection = DatabaseFactory.new_connection(DatabaseFactoryEnum.PROD)
    cursor = connection.cursor()
    self.assertIsInstance(connection, Connection)
    self.assertIsInstance(cursor, Cursor)

  def test_connects_to_test_database(self):
    connection: Connection = DatabaseFactory.new_connection(DatabaseFactoryEnum.DEV)
    cursor = connection.cursor()
    self.assertIsInstance(connection, Connection)
    self.assertIsInstance(cursor, Cursor)
  
  def test_migration(self):
    conn = DatabaseFactory.new_connection(DatabaseFactoryEnum.DEV)
    DatabaseFactory.migrate(conn)
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='connections';")
    result = cur.fetchall()[0][0]
    self.assertTrue(result == "connections")
    
