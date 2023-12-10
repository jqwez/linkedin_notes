
class ConnectionDAO:
  def __init__(self, 
               _id: int, 
               name: str, 
               linkedin: str, 
  ):
    self.id = _id
    self.name = name
    self.linkedin = linkedin

  def __repr__(self):
    return f"ConnectionDAO(_id={self.id}, name={self.name}, linkedin={self.linkedin})"
  
  def __str__(self):
    return f"Connection: {self.name}, {self.linkedin}"
  
  def __eq__(self, other: object) -> bool:
    if self.id == other.id and self.name == other.name and self.linkedin == other.linkedin:
      return True
    else:
      return False

  @staticmethod
  def from_entry(database_entry):
    if database_entry is None:
      return None
    _id, name, url = database_entry
    return ConnectionDAO(_id, name, url)
