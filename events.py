#!/bin/python3
import random

def selectEvent(govt, turn):
  eventlist = [ai, crop_surplus, job_surplus, plague, renaissance, asteroid, natural_disaster, new_city, scandal]
  print("SEASON {0}".format(turn))
  return random.choice(eventlist)(govt.stats)

def ai(stats):
  result = None
  ### science
  if stats['Science'] < 5:
    result = "An AI has been developed, but your science is too low, the AI attacks your banks and you lose 20% of your money and your popularity falls 10%!"
  else:
    result = "An AI has been developed and your science is high enough to deal with it! Your money increases 20% and your popularity rises 10%!"
  return result

def asteroid(stats):
  return "An asteroid is approaching. You have two options, either you spend 20% of your money and destroy the asteroid with missiles, or 20% of your people will die!"

def crop_surplus(stats):
  ### food
  result = None
  if stats['Food'] < 7:
    result = "Fields are producing a ton of crop! But your Food stat is too low to take advantage of it! Your population falls 20% and your popularity falls 10%"
  else:
    result = "Fields are producing a ton of crop! and your Food stat is high enough to take advantage of it! Your population rises 20% and your popularity rises 10%"
  return result

def job_surplus(stats):
  ### employment
  result = None
  if stats['Employment'] < 6:
    result = "Markets are booming, but your Employment is too low to take advantage of it! Your money falls by 20% and your popularity falls 10%"
  else:
    result = "Markets are booming! Your money increases 20% and your popularity rises 10%!"
  return result


def natural_disaster(stats):
  disasters = [
    " tsunami has hit!",
    " volcano erupted!",
    " tornado has hit!",
    " hurricane has hit!",
    " solar flare has hit!",
    " blizzard has hit!",
    "n avalanche occurred!",
    "n earthquake has hit!",
  ]
  
  result = "A{0} 35% of your population has died".format(random.choice(disasters))
  return result

def new_city(stats):
  return "You've built a new city, gain 5% to your population"

def plague(stats):
  return "Your people were affected by a Devistating Plague, 50% of your population has died!"

def renaissance(stats):
  ### culture
  result = None
  if stats['Culture'] < 8:
    result = "There is a Renaissance, but your culture is too low, your citizens are mad, your popularity falls 20%!"
  else:
    result = "There is a Renaissance, and your culture is high! Your citizens are thrilled, your popularity and culture rise 20%!"
  return result

def scandal(stats):
  return "You messed up. Let's just say a scandal is about to break out you have two options, either you spend 50% of money and keep everyone quiet, or lose 40% of your popularity!"
