#! /bin/python3

name= {
  0:' ____    ____  ______  ____  ___   ____       ____   __ __  ____  _      ___      ___  ____    _____',
  1:'|    \  /    ||      ||    |/   \ |    \     |    \ |  |  ||    || |    |   \    /  _]|    \  / ___/',
  2:'|  _  ||  o  ||      | |  ||     ||  _  |    |  o  )|  |  | |  | | |    |    \  /  [_ |  D  )(   \_ ',
  3:'|  |  ||     ||_|  |_| |  ||  O  ||  |  |    |     ||  |  | |  | | |___ |  D  ||    _]|    /  \__  |',
  4:'|  |  ||  _  |  |  |   |  ||     ||  |  |    |  O  ||  :  | |  | |     ||     ||   [_ |    \  /  \ |',
  5:'|  |  ||  |  |  |  |   |  ||     ||  |  |    |     ||     | |  | |     ||     ||     ||  .  \ \    |',
  6:'|__|__||__|__|  |__|  |____|\___/ |__|__|    |_____| \__,_||____||_____||_____||_____||__|\_|  \___|'
}

Description= ''

def creation(Govt):
  plutocracy = Govt('plutocracy', 'Rule by the wealthy; a system wherein governance is indebted to, dependent upon or heavily influenced by the desires of the rich.', {'Culture':5,'Employment':5,'Food':6,'Military':5,'Science':5})
  technocracy = Govt('technocracy', 'Rule by the educated and/or technical experts; a system of governance where people who are skilled or proficient govern in their respective areas of expertise in technology would be in control of all decision making.', {'Culture':6,'Employment':8,'Food':6,'Military':3,'Science':10})
  meritocracy = Govt('meritocracy', 'Rule by the meritorious; a system of governance where groups are selected on the basis of people\'s ability, knowledge in a given area, and contributions to society.', {'Culture':7,'Employment':7,'Food':5,'Military':6,'Science':6})
  kraterocracy = Govt('kraterocracy', 'Rule by the strong; a system of governance where those who are strong enough seize power through physical force, social maneuvering or political cunning.', {'Culture':2,'Employment':4,'Food':4,'Military':10,'Science':3})
  autocracy = Govt('autocracy', 'Power resides in the hands of one single person.', {'Culture':3,'Employment':3,'Food':3,'Military':5,'Science':3})
  oligarchy = Govt('oligarchy', 'Rule by a small number of people. Not based on class.', {'Culture':5,'Employment':4,'Food':5,'Military':6,'Science':5})
  absoluteMon = Govt('absolute monarchy', 'A traditional and historical system where the monarch exercises ultimate governing authority as head of state and head of government.', {'Culture':7,'Employment':4,'Food':5,'Military':6,'Science':3})
  constitutionalMon = Govt('constitutional monarchy', 'The monarch\'s powers are limited by law or by a formal constitution, usually assigning them to those of the head of state.', {'Culture':7,'Employment':5,'Food':5,'Military':7,'Science':3})
  bankocracy = Govt('bankocracy', 'Rule by banks; a system of governance with excessive power or influence of banks and other financial authorities on public policy-making.', {'Culture':4,'Employment':8,'Food':5,'Military':5,'Science':4})
  corporatocracy = Govt('corporatocracy', 'Rule by corporations; a system of governance where an economic and political system is controlled by corporations or corporate interests.', {'Culture':3,'Employment':8,'Food':6,'Military':7,'Science':3})
  nepotocracy = Govt('nepotocracy', 'Rule by nephews; favouritism granted to relatives regardless of merit; a system of governance in which importance is given to the relatives of those already in power, like a nephew (where the word comes from).', {'Culture':5,'Employment':5,'Food':5,'Military':5,'Science':5})
  kakistocracy = Govt('kakistocracy', 'Rule by the stupid; a system of governance where the worst or least-qualified citizens govern or dictate policies.', {'Culture':4,'Employment':5,'Food':7,'Military':2,'Science':1})
  democracy = Govt('democracy', 'Rule by a form of government in which all the people of a state or polity are involved in making decisions about its affairs.', {'Culture':5,'Employment':5,'Food':5,'Military':5,'Science':5})
  republic = Govt('republic', 'Rule by a form of government in which the people, or some significant portion of them, have supreme control over the government and where offices of state are elected or chosen by elected people.', {'Culture':5,'Employment':5,'Food':5,'Military':5,'Science':5})
  options = [plutocracy, technocracy, meritocracy, kraterocracy, autocracy, oligarchy, absoluteMon, constitutionalMon, bankocracy, corporatocracy, nepotocracy, kakistocracy, democracy, republic]
  list_of_names = []
  #months = set(month.lower() for month in ("January", "February", "March", "April","May", "June", "July"))
  list_of_names = set(options[names].name.lower() for names in range(0, len(options)))
  #for names in range(0, len(options)):
  #  list_of_names.append(options[names].name.lower())
  yield options
  yield plutocracy
  yield technocracy
  yield meritocracy
  yield kraterocracy
  yield autocracy
  yield oligarchy
  yield absoluteMon
  yield constitutionalMon
  yield bankocracy
  yield corporatocracy
  yield nepotocracy
  yield kakistocracy
  yield democracy
  yield republic
  yield list_of_names
