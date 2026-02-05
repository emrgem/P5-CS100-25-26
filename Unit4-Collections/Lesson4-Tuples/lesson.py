# Creating a Tuple
spawn_point = (100, 200)
print(type(spawn_point))

spawn_point = [100, 200]
print(type(spawn_point))

#Turn List into a Tuple
spawn_point = tuple(spawn_point)
print(type(spawn_point))

# Empty Tuple
empty_tuple = tuple()
# Single Value Tuple
single_val_tuple = (12) #int
print(type(single_val_tuple))

single_val_tuple = (12,) #, indicates this is a tuple
single_val_tuple = 12, #, parenthesis is optional
print(type(single_val_tuple))

#Tuples are immutable - can't change 
# spawn_point[0] = 150 # TypeError

# Reading Tuples: Indexing
song = ("Blinding Lights", "2020", "Wake me up")
print(song[0]) # first item
print(song[-1])# last item

# Reading Tuples: Other Operations
print(len(song)) #3
print("Wake me up" in song) # True

#Tuple Unpacking
song = ("Bad Guy", "Billie Eilish",2019)
title, artist, year = song
print(title)
print(artist)
print(year)

# Multiple return values - returns a tuple
def get_min_max(numbers):
    return min(numbers), max(numbers)
result = get_min_max([5,2,8,1,9])
print(result) # (1,9)
min, max = result
print(min)

# Tuples can be a dict key
locations = {
    (0,0): "spawn",
    (10,5): "treasure"
}
print(locations[(10,5)])

print(f"List Directory {dir([])}")
print(f"List Methods Lenght:{len(dir([]))}")

print(f"Tuple Directory {dir(tuple())}")
print(f"Tuple Methods Lenght:{len(dir(tuple()))}")