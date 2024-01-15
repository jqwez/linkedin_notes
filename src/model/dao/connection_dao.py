class ConnectionDAO:
    def __init__(self, _id: str, name: str, linkedin: str, company: str = None):
        self.id: str = _id
        self.name: str = name
        self.linkedin: str = linkedin
        self.company: str = company

    def __repr__(self):
        return f"ConnectionDAO(_id='{self.id}', name='{self.name}', linkedin='{self.linkedin}', company='{self.company}')"

    def __str__(self):
        return f"Connection: {self.name}, {self.linkedin}"

    def __eq__(self, other: object) -> bool:
        if (
            self.id == other.id
            and self.name == other.name
            and self.linkedin == other.linkedin
        ):
            return True
        else:
            return False

    def set(self, field: str, value: str):
        self.__setattr__(field, value)

    def get(self, field: str) -> str:
        value = self.__getattribute__(field)
        return value if value else ""

    @staticmethod
    def from_entry(database_entry):
        if database_entry is None:
            return None
        _id, name, url, company = database_entry
        return ConnectionDAO(_id, name, url, company)
