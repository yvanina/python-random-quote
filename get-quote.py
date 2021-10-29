import random

def primary():
  print("Welcome to my bot!")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  
  last = len(quotes) - 1
  
  #rnd2 = random.randint(0, last)

  counter = 0
  for counter in range(0,last):
    counter+=1
    rnd1 = random.randint(0, last)
    print("Quote " + str(counter) + " of the day is: " + quotes[rnd1])

    #print("The quote" + str(counter) + "of the day is: " + quotes[rnd2])

  quest = input ("Teach your bot a quote by typing it here:\n")
  
  #you ahve to fix this. currently there are 2 extra lines, before the new lines a added. 
  with open("quotes.txt", "a") as f:
    f.seek(0)
    if len(quotes) > 0:
      f.write("\n")
      f.write(quest)


if __name__== "__main__":
  primary()
