# # def expensive_function(x,y):
# #     key = (x,y)

# #     if key not in cache: # if n is not a key in the cache
# #         cache[key] = whatever_expensive_thing_here()
# #     return cahce[key]



# # Let's sort a dictionary / hash table

# d = {
#     'foo': 21,
#     'bar': 187,
#     'qux': 2,
# }

# items = list(d.items())

# #Sort ascending by key
# items.sort()
# print(items)

# #Sort decending by key
# items.sort(reverse=True)

# print(items)
# print(dict(items))

# #Sort ascending by value
# # def get_key(e):# e is going to be the tuple
# #     # Return the thing that we want to sort by
# #     return e[1]

# # items.sort(key=get_key, reverse=True)

# items.sort(key=lambda e: e[1])
# print(items)

def print_letter_count(s):
    counts = {}

    for c in s:
        #c = c.lower() #case sensitive
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1

    items = list(counts.items())
    items.sort(key=lambda e: e[1], reverse=True)

    print(items)
print_letter_count('aaabbcbcaAA!@')
