# dictionaries are like lists
# but, instead of an integer index, you can access it by it's key
# the key can be: strings, integers, floats
# dictionaries are unordered
consoles = { "nintendo":"wii", "microsoft":"xbox", "sony":"playstation" }
print(consoles)
print(consoles["microsoft"])

print("sony" in consoles)
print("atari" in consoles)
print("philco" not in consoles)
