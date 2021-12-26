import string, itertools

#password = input("Enter password: ")

password = "abc"

characters = string.printable

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