import unittest
import tkinter as tk
from tkinter import ttk

from view.main_window import MainWindow

class MainWindowTest(unittest.TestCase):
  main_window = MainWindow()
  class TestFrame(ttk.Frame):
    def __init__(self, master=None, **kwargs):
      super().__init__(master, **kwargs)
      self.label = ttk.Label(self, text="test").grid(column=0, row=0)

  def test_add_view_only_accepts_string_as_first_argument(self):
    self.main_window.add_view("test_frame", self.TestFrame)
    for item in [1, self.TestFrame]:
      with self.assertRaises(TypeError):
        self.main_window.add_view(item, self.TestFrame)

  def test_add_view_only_accepts_Frame_as_second_argument(self):
    for item in [self.TestFrame, tk.Frame, ttk.Frame]:
      self.main_window.add_view("test frame", item)
    for item in [1, "some_string", tk.Label, ttk.Button, ttk.Panedwindow]:
      with self.assertRaises(TypeError):
        self.main_window.add_view("string", item)

  def test_transition_view(self):
    pass