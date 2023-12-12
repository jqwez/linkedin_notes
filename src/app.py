import sys
from controller import startup




def main(args=None):
  startup.start_view()




if __name__ == "__main__":
  args = sys.argv[1:]
  main(args)