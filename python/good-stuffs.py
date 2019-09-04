#create a dictionary character to index and index to charactare
# chars contains a list of unique charcatrers
data = "this is the ice cold, michelle pifer that gold"
chars = set(data)
char_to_ix = { ch:i for i,ch in enumerate(sorted(chars)) }
ix_to_char = { i:ch for i,ch in enumerate(sorted(chars)) }
print(ix_to_char)