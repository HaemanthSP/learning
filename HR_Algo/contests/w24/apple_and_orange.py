# Read all the inputs
house = map(int,raw_input().split())
trees_loc = map(int,raw_input().split())
m, n = map(int,raw_input().split())
f1_dists = map(int,raw_input().split())
f2_dists = map(int,raw_input().split())

# Calculate fruits actual location
f1_loc = [i+trees_loc[0] for i in f1_dists]
f2_loc = [i+trees_loc[1] for i in f2_dists]

# Count no of fruits fell on house
f1_count = sum([1 for i in f1_loc if i in range(house[0],house[1]+1)])
f2_count = sum([1 for i in f2_loc if i in range(house[0],house[1]+1)])

# Print the count
print f1_count
print f2_count
