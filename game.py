#!/bin/python3
from setup import info
import random

def main():
  print("Welcome to")
  gamename()
  print("I am now going to list off the full list of starting Governments that you can choose to start as.\nIf you need a definitition of any of them (or details of their starting Stats),  please type \'Help\' and hit Enter, otherwise please type the name of the Government type you would like to start with!")
  fulllist = "Please select one of the following: "
  for name in range(0, len(info.Gov_names)):
    fulllist += info.Gov_names[name].title()
    if name == (len(info.Gov_names)-1):
      break
    else:
      fulllist += ", "
  while True:
    choice = input(fulllist+"\n")
    if "help" in choice.lower():
      for name in range(0, len(info.Gov_names)):
        print("\nType: {0}\n  Definition: {1}\n   Stats:\n   ".format(info.Gov_names[name].title(), info.Gov_defs[name]),end='')
        for stat in range(0, len(info.Stats)-1):
          print("{0}: ".format(info.Stats[stat]),end='')
          print(info.Gov_stats.get(info.Gov_names[name])[stat],end=' ')
        print()
    elif choice.lower() in fulllist.lower():
      print("Okay, you want to play as a {0}. Which means your starting stats will be:".format(choice))
      print("  ",end='')
      for stat in range(0, len(info.Stats)-1):
        print("{0}: ".format(info.Stats[stat]),end='')
        print(info.Gov_stats.get(choice.lower())[stat],end=' ')
      print()
      break
    else:
      print("Please choose one from the list or ask for help!")

def gamename():
  for line in range(0, len(info.name)):
    print(info.name[line])

if __name__ == "__main__":
  main()
