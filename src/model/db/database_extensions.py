from datetime import datetime
import sqlite3


class DatabaseExtensions:

  def __init__(self) :
    self.to_adapt: list[tuple[type, function]] = [(datetime, self.adapt_datetime_iso)]
    self.to_convert: list[tuple[str, function]] = [("datetime", self.convert_datetime)]

  def apply_extensions(self):
    for item in self.to_adapt:
      type_adapted, adapter = item
      sqlite3.register_adapter(type_adapted, adapter)
    for item in self.to_convert:
      type_converted, converter = item
      sqlite3.register_converter(type_converted, converter)
  
  def adapt_datetime_iso(self, val: datetime):
    return val.isoformat()

  def convert_datetime(self, val: str):
    return datetime.fromisoformat(val.decode())
  




