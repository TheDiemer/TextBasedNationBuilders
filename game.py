#!/bin/python3
from setup import info, selection, start

def main():
  start.start()
  choose = Govt()
  playinggovt = selection.selection(choose)

class Govt:
  name = ""
  definition = ""
  stats = {'Culture':5,'Employment':5,'Food':5,'Military':5,'Money':5,'Science':5}

if __name__ == "__main__":
  main()
