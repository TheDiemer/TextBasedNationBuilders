#!/bin/python3
from events import options
import random

def main():
  print("Welcome to Nation Builders!\nI am going to list off the full list of the forms of starting Governments, if you need a definitition of any of them, please type \'Help <GOVERNMENT>\' and hit Enter, otherwise please type the name of the Government type you would like to start with!")
  for name in range(0, len(options.Gov_names)):
    print(options.Gov_names[name])
  #choice = random.randint(0, len(options.Gov_names))
  #print(options.Gov_names[choice])
  #print(options.Gov_defs[choice])


if __name__ == "__main__":
  main()
