import random

subjects = [
  "Virat Kohli",
  "Mamta Banerjee",
  "Rekha Gupta",
  "Samrat chaudhary",
  "Mr Bean",
  "Shahrukh Khan",
  "Messi",
  "Donald Trump",
  "Asim Munir",
  "A group of monkeys",
  "A group of dogs"
] 

actions = [
  "eats",
  "dances",
  "laughs",
  "goes",
  "jumps",
  "celebrates",
  "is very funny",
  "declares war",
  "travels a lot",
  "launches"
]

places = [
  "at red fort",
  "in patna metro",
  "samosa",
  "buffalo",
  "temperature",
  "during shower",
  "during ipl match",
  "at India Gate",
  "pizza and burger"

]

while True:
  subject = random.choice(subjects)
  action = random.choice(actions)
  place_or_thing = random.choice(places)

  headline = f" BREAKING NEWS: {subject} {action} {place_or_thing} "
  print("\n" + headline)

  user_input = input("\nDo you want another headline? (yes/no)").strip().lower()
  if user_input == "no":
    break

print("\nThanks for using the Fake News Headline Generator. \nHave a fun day.")
