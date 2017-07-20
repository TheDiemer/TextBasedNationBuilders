#!/bin/python3
from setup import info, selection, start

class Govt(object):
  def __init__(self, name, definition, stats = {'Culture':5,'Employment':5,'Food':5,'Military':5,'Money':5,'Science':5}):
    self.name = name
    self.definition = definition
    self.stats = stats

def main():
  #options, plutocracy, technocracy, meritocracy, kraterocracy, autocracy, oligarchy, absoluteMon, consitutionalMon, bankocracy, corporatocracy, nepotocracy, kakistocracy, democracy, republic = info.creation(Govt)
  #print(plutocracy.name)
  #print(plutocracy.definition)
  #print(plutocracy.stats.get('Food'))
  #plutocracy.stats['Food'] = 7
  #print(plutocracy.stats.get('Food'))
  #for thing in range(0, len(options)):
  #  print(options[thing].name)
  #  print(options[thing].stats)
  start.start()
  playingGovt = selection.selection(Govt)
  selection.printTypeDefStats(playingGovt)

if __name__ == "__main__":
  main()
