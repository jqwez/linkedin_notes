import unittest

from model.dao.connection_dao import ConnectionDAO

class ConnectionDAOTest(unittest.TestCase):

   def test_dao_must_have_minimum_args(self):
      with self.assertRaises(TypeError):
         connection_dao = ConnectionDAO()

   def test_dao_is_created(self):
     conection_dao = ConnectionDAO(
        10,
        "jeremy",
        "linkedin.com/in/jeremy"
     )
