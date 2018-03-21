import  collections
lookup = {}
lookup = dict()

lookup = dict(age = 42, loc='Italy')

print(lookup)

print(lookup['loc'])

if 'cat' in lookup:
    print("Found cat in lookup")
else:
    print("Didn't find cat in lookup the first time")

lookup['cat']='Fun Code Demo'

if 'cat' in lookup:
    print("Found cat in lookup")
    print(lookup['cat'])
else:
    print("Still didn't find cat in lookup")


class Wizard:
    def __init__(self, name, level):
        self.name = name
        self.level = level

gandolf = Wizard(name="Gandolf", level=10)

print(gandolf.__dict__)

User = collections.namedtuple('User', 'id, name, email')

users = [
    User(1, 'user1', 'user1@gmail.com'),
    User(2, 'user2', 'user2@gmail.com'),
    User(3, 'user3', 'user3@gmail.com'),
]

lookup = {}
for u in users:
    lookup[u.id] =u

print(lookup[3])

#Keys must be unique
bad_dict = {"joe":"amy", 'joe':"sue"}
print(bad_dict)