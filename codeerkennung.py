import string, itertools

#password = input("Enter password: ")
print("Tippen Sie ein Paswort aus vier Zahlen")


def pruefung(password):
    if len(password) > 4:
        print("Ihre Zahl hat mehr als 4 Zeichen. Tippen Sie ein Paswort aus vier Zahlen")
        return False
    else:
        return True
      
while True:      
      
  password = input() 
  if not pruefung(password):
    continue 
   
  characters = string.digits
  def iter_all_strings():
      length = 1
      while True:
          for s in itertools.product(characters, repeat=length):
              yield "".join(s)
          length +=1

  for s in iter_all_strings():
      print(s)
      if s == password:
          print('Password is {}'.format(s))
          break  