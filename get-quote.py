import random
def primary():
   #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = 20
  rnd = random.randint(0, last)
  print(random.choices(quotes))
  print(random.choices(quotes))
if __name__== "__main__":
  primary()
