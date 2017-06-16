#!/bin/python3
from setup import info
import random

def main():
  print("\033c")
  print("Welcome to")
  gamename()
  print("\nI am now going to list off the full list of starting Governments that you can choose to start as.\nIf you need a definitition of any of them (or details of their starting Stats),  please type \'Help\' and hit Enter, or add a government after \'Help\' to learn about that specific one \'Help Kraterocracy\', otherwise please type the name of the Government type you would like to start with!\n")
  fulllist = "Please select one of the following: "
  for name in range(0, len(info.Gov_names)):
    fulllist += info.Gov_names[name].title()
    if name == (len(info.Gov_names)-1):
      break
    else:
      fulllist += ", "
  while True:
    choice = input(fulllist+"\n")
    if choice == '':
      print("\033cPlease choose one from the list or ask for help!\n")
    elif "help" in choice.lower():
      specific = None
      for name in range(0, len(info.Gov_names)):
        if (info.Gov_names[name] == choice.lower().split(' ',1)[1]):
          specific = choice.lower().split(' ',1)[1]
      print("\033c")
      if specific == None:
    ### Default Behavior, print all of the types and all of their definitions
        for name in range(0, len(info.Gov_names)):
          print("\nType: {0}\n  Definition: {1}\n   Stats:\n   ".format(info.Gov_names[name].title(), info.Gov_defs[name]),end='')
          for stat in range(0, len(info.Stats)-1):
            print("{0}: ".format(info.Stats[stat]),end='')
            print(info.Gov_stats.get(info.Gov_names[name])[stat],end=' ')
          print("\n")
      else:
    ### If you specify a type that you need help with
        print("\nType: {0}\n  Definition: {1}\n   Stats:\n   ".format(specific.title(), info.Gov_defs[info.Gov_names.index(specific)]), end='')
        for stat in range(0, len(info.Stats)-1):
          print("{0}: ".format(info.Stats[stat]),end='')
          print(info.Gov_stats.get(specific.lower())[stat],end=' ')
        print("\n") 
    elif choice.lower() in fulllist.lower():
      valid = False
      for name in range(0, len(info.Gov_names)):
        if choice.lower() == info.Gov_names[name]:
          valid = True
      if valid == True:
        print("\033cOkay, you want to play as a {0}. Which means your starting stats will be:".format(choice.title()))
        print("  ",end='')
        for stat in range(0, len(info.Stats)-1):
          print("{0}: ".format(info.Stats[stat]),end='')
          print(info.Gov_stats.get(choice.lower())[stat],end=' ')
        print()
        break
      else:
        print("\033cPlease choose one from the list or ask for help!\n")
    else:
      print("\033cPlease choose one from the list or ask for help!\n")

def gamename():
  for line in range(0, len(info.name)):
    print(info.name[line])

if __name__ == "__main__":
  main()
