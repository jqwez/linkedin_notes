

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


