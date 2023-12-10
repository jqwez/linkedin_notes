import unittest

from model.dao.connection_dao import ConnectionDAO

class ConnectionDAOTest(unittest.TestCase):
  def test_dao_is_created(self):
     conectionDao = ConnectionDAO(
        10,
        "jeremy",
        "linkedin.com/in/jeremy"
     )
