from unittest import TestCase
from datetime import datetime
from uuid import uuid4

from model.dao.interaction_dao import InteractionDAO


class InteractionDAOTest(TestCase):
    def test_dao_must_have_minimum_args(self):
        with self.assertRaises(TypeError):
            dao = InteractionDAO()

    def test_dao_is_created(self):
        dao = InteractionDAO(
            _id=str(uuid4()),
            connection_id=str(uuid4()),
            notes="same notes",
            date_created=datetime.now(),
            date_interaction=datetime.now(),
        )

    def test_from_entry_returns_dao(self):
        return
