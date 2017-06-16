#!/bin/python3
from setup import info

def start():
  print("\033cWelcome to")
  gamename()

def gamename():
  for line in range(0, len(info.name)):
    print(info.name[line])
