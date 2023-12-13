from datetime import datetime


class InteractionDAO:
    def __init__(
        self,
        _id: int,
        connection_id: str,
        notes: str,
        date_created: datetime,
        date_interaction: datetime,
    ):
        self.id = _id
        self.connection_id = connection_id
        self.notes = notes
        self.date_created = date_created
        self.date_interaction = date_interaction

    def __repr__(self):
        return f"InteractionDAO(_id={self.id}, notes={self.notes}, date_created={self.date_created}, date_interaction={self.date_interaction})"

    def __str__(self):
        return f"Interaction: date={self.date_interaction} notes={self.notes[0:100]}"

    def __eq__(self, other: object) -> bool:
        if self.id == other.id:
            return True
        else:
            return False

    @staticmethod
    def from_entry(database_entry):
        if database_entry is None:
            return None
        _id, connection_id, notes, date_created, date_interaction = database_entry
        return InteractionDAO(_id, connection_id, notes, date_created, date_interaction)
