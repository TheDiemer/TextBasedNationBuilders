#!/bin/python3
from setup import info

def selection(Govt):
  print("\nI am now going to list off the full list of starting Governments that you can choose to start as.\nIf you need a definitition of any of them (or details of their starting Stats),  please type \'Help\' and hit Enter, or add a government after \'Help\' to learn about that specific one \'Help Kraterocracy\', otherwise please type the name of the Government type you would like to start with!\n")
  fulllist = "Please select one of the following: "

  options, plutocracy, technocracy, meritocracy, kraterocracy, autocracy, oligarchy, absoluteMon, consitutionalMon, bankocracy, corporatocracy, nepotocracy, kakistocracy, democracy, republic = info.creation(Govt)


  for name in range(0, len(options)):
    fulllist += options[name].name.title()
    if name == (len(options)-1):
      break
    else:
      fulllist += ", "
  while True:

    ### Store the user input as variable `choice` to be used throughout
    choice = input(fulllist+"\n")

    ### You just hit enter
    if choice == '':
      print("\033cPlease choose one from the list or ask for help!\n")

    ### You need help understanding the settings
    elif "help" in choice.lower():
      specific = None

      ### Check if you specified a type to get help on
      for name in range(0, len(options)):
        try:
          if (options[name].name == choice.lower().split(' ',1)[1]):
            specific = choice.lower().split(' ',1)[1]
        except IndexError:
          pass

      ### Clear the screen and move on
      print("\033c")

      ### Default Behavior, print all of the types and all of their definitions
      if specific == None:
        for name in range(0, len(options)-1):
          print("\nType: {0}\n  Definition: {1}\n   Stats:\n    ".format(options[name].name.title(), options[name].definition),end='')
          for stat in range(0, len(info.Stats)):
            print("{0}: ".format(info.Stats[stat]),end='')
            print(info.Gov_stats.get(info.Gov_names[name])[stat],end=' ')
          print("\n")

      ### If you specify a type that you need help with
      else:
        print("\nType: {0}\n  Definition: {1}\n   Stats:\n    ".format(specific.title(), info.Gov_defs[info.Gov_names.index(specific)]), end='')
        for stat in range(0, len(info.Stats)):
          print("{0}: ".format(info.Stats[stat]),end='')
          print(info.Gov_stats.get(specific.lower())[stat],end=' ')
        print("\n")

    ### You put something and it matched with something the list of names 
    elif choice.lower() in fulllist.lower():
      ### Validate what you selected
      valid = False
      for name in range(0, len(info.Gov_names)):
        if choice.lower() == info.Gov_names[name]:
          valid = True
      ### You entered a full name of one of the options
      if valid == True:
        print("\033cOkay, you want to play as a {0}. Which means your starting stats will be:".format(choice.title()))
        print("  ",end='')
        answer.name = choice.title()
        answer.definition = info.Gov_defs[info.Gov_names.index(choice.lower())]
        for stat in range(0, len(info.Stats)):
          print("{0}: ".format(info.Stats[stat]),end='')
          print(info.Gov_stats.get(choice.lower())[stat],end=' ')
          answer.stats[info.Stats[stat]] = info.Gov_stats.get(choice.lower())[stat]
        print()
        return answer
        break
      ### False positive, you did not enter a full name or something completely valid
      else:
        print("\033cPlease choose one from the list or ask for help!\n")

    ### You didn't enter a valid choice of help or something from the list
    else:
      print("\033cPlease choose one from the list or ask for help!\n")
