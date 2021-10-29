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
    print("Quote " + str(counter) + " of the day is: " + quotes[rnd1], end = "")
    #print("The quote" + str(counter) + "of the day is: " + quotes[rnd2])



if __name__== "__main__":
  primary()
