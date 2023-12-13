import unittest
from sqlite3 import Connection, Cursor
from datetime import datetime
from model.db.database_factory import DatabaseFactory, DatabaseFactoryEnum
from model.db.database_extensions import DatabaseExtensions

class DatabaseExtensionTest(unittest.TestCase):

  def setUp(self):
    self.conn = DatabaseFactory.new_connection(DatabaseFactoryEnum.DEV)
    self.cur = self.conn.cursor()
    self.cur.execute("CREATE TABLE testing (time_test DATETIME);")

  def tearDown(self):
    self.cur.execute("DROP TABLE testing;")
    self.conn.commit()
    pass

  def test_table_accepts_datetime(self):
    current_time = datetime.now()
    self.cur.execute("INSERT INTO testing (time_test) VALUES (?)", (current_time,))
  
  def test_datetime_object_created_from_database(self):
    # required detect_types on connection 
    current_time = datetime.now()
    self.cur.execute("INSERT INTO testing (time_test) VALUES (?)", (current_time,))
    self.cur.execute("SELECT * from testing;")
    data = self.cur.fetchall()
    self.assertIsInstance(data[0][0], datetime)