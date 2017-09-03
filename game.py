#!/bin/python3
from setup import info, selection, start
import events

class Govt(object):
  def __init__(self, name, definition, stats = {'Culture':5,'Employment':5,'Food':5,'Military':5,'Science':5}):
    self.name = name
    self.definition = definition
    self.stats = stats

class GameStats(object):
  def __init__(self, tier1 = {}, tier2 = {}):
    self.tier1 = tier1
    self.tier2 = tier2

def main():
  #options, plutocracy, technocracy, meritocracy, kraterocracy, autocracy, oligarchy, absoluteMon, consitutionalMon, bankocracy, corporatocracy, nepotocracy, kakistocracy, democracy, republic, list_of_names= info.creation(Govt)
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
  #selection.printTypeDefStats(playingGovt)
  turn = 1
  maxTurn = 5
  response = None
  while turn <= maxTurn:
    #if response != None:
    #  print("You said {0}".format(response))
    response = input(events.selectEvent(playingGovt, turn) + "\n")
    turn = turn + 1

if __name__ == "__main__":
  main()
