#!/bin/python3
from setup import info

def selection(Govt):
  print("\nI am now going to list off the full list of starting Governments that you can choose to start as.\nIf you need a definitition of any of them (or details of their starting Stats),  please type \'Help\' and hit Enter, or add a government after \'Help\' to learn about that specific one \'Help Kraterocracy\', otherwise please type the name of the Government type you would like to start with!\n")
  fulllist = "Please select one of the following: "

  options, plutocracy, technocracy, meritocracy, kraterocracy, autocracy, oligarchy, absoluteMon, consitutionalMon, bankocracy, corporatocracy, nepotocracy, kakistocracy, democracy, republic, list_of_names = info.creation(Govt)

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
        for name in range(0, len(options)):
          printTypeDefStats(options[name])

      ### If you specify a type that you need help with
      else:
        ### Determine the name of the government type that you asked for help on
        specific_number = None
        for number in range(0, len(options)):
          if options[number].name == specific.lower():
            specific_number = number
          else:
            pass
        printTypeDefStats(options[specific_number])

    ### You put something and it matched with something the list of names 
    elif choice.lower() in list_of_names:
      ### Validate what you selected
      valid = None
      for name in range(0, len(options)):
        if choice.lower() == options[name].name.lower():
          valid = name

      ### You entered a full name of one of the options
      if valid != None:
        print("\033cOkay, you want to play as a {0}. Which means your starting stats will be:".format(options[valid].name.title()))
        print("  ",end='')
        ### Setting the decided government type as the answer variable so that can be returned and used throughout
        tempStats = {}
        i = 0
        for key, value in options[valid].stats.items():
          print('{0}: '.format(key),end='')
          print(value,end='')
          if i < 5:
            print(', ',end='')
          i = i + 1
          tempStats[key] = value
        print()
        answer = Govt(options[valid].name.title(), options[valid].definition, tempStats)
        return answer
        break

      ### False positive, you did not enter a full name or something completely valid
      else:
        print("\033cPlease choose one from the list or ask for help!\n")

    ### You didn't enter a valid choice of help or something from the list
    else:
      print("\033cPlease choose one from the list or ask for help!\n")


def printTypeDefStats(government):
  print("\nType: {0}\n  Definition: {1}\n   Stats:\n    ".format(government.name.title(), government.definition),end='')
  i = 0
  for key, value in government.stats.items():
    print('{0}: '.format(key),end='')
    print(value,end='')
    if i < 5:
      print(', ',end='')
    i = i + 1
  print("\n")
