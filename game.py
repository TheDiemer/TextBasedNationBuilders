#!/bin/python3
from setup import info, selection, start
import events

class Govt(object):
  def __init__(self, name, definition, stats = {'Culture':5,'Employment':5,'Food':5,'Military':5,'Science':5}):
    self.name = name
    self.definition = definition
    self.stats = stats

class GamePubStats(object):
  def __init__(self, Money, Perception, Population):
    self.Money = Money
    self.Perception = Perception
    self.Population = Population

class GamePrivStats(object):
  def __init__(self, Happiness, Env_Health, Education, Industry, Pop_growth):
    self.Happiness = Happiness
    self.Env_Health = Env_Health
    self.Education = Education
    self.Industry = Industry
    self.Pop_growth = Pop_growth

def Rules():
  Govt_stat_changes= {
    'culture is changed when happiness, education, and money change',
    'employment is changed when industry, education, and money change. And when employment changes, so does happiness',
    'food is changed when env_health, industry, and money change. And when food changes, so does happiness and pop_growth',
    'military is changed when industry, science, and money change. And when military changes, so does happiness',
    'science is changed when education and money change. And when science changes, so does industry and env_health'
  }
  GamePubStats_changes = {
    '',
    '',
    ''
  }
  GamePrivStats_changes = {
    '',
    '',
    '',
    '',
    ''
  }

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
