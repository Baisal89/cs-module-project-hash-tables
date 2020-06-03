
class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return f'HashtableEntry({repr(self.key)},{repr(self.value)})'

data = [None, None, None, None, None, None, None]

def my_hashing_function(s):
    string_bites = s.encode()

    total = 0

    for b in string_bites:
        total += b

    return total


def get_slot(s):
    hash_val = my_hashing_function(s)
    return hash_val % len(data)

def get(key):
    slot = get_slot(key)
    hash_entry = data[slot]

    if hash_entry is not None:
        return hash_entry.value
    return None


# define get():
def put(key, value):
    slot = get_slot(key)
    data[slot] = HashTableEntry(key, value)

def delete(key):
    put(key, None)

print(get_slot('Biasal'))
print(get_slot('Etna'))
print(get_slot('Ana'))
print(get_slot('Anisa'))
print(get_slot('Sabrina'))
# put('Ana', 3490)
# put('Sabrina', 6864)
# put('Anisa', 3290)

# #print(data)


# print(get('Ana'))
# print(get('Sabrina'))
# print(get('ric'))
