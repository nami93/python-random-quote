def add():
  print("valami")
  f = open("quotes.txt", "a");
  
  f.write("new quote");

  f.close()

if __name__== "__main__":
  add()