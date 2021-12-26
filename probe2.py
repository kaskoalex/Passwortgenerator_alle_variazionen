import string

from itertools import chain, product
def bruteforce(charset, maxlength):
    return (''.join(candidate)
        for candidate in chain.from_iterable(product(charset, repeat=i)
        for i in range(1, maxlength + 1)))

print(bruteforce)    
print(list(bruteforce('abcde', 2)))

matched="abd "

for attempt in bruteforce(string.ascii_lowercase, 3):
    print(attempt)
    # match it against your password, or whatever
    if matched:
        break
    print(attempt)     