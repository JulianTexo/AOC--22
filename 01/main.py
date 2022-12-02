import os
import sys

with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    contents = [line.rstrip() for line in f]

inventories = []
sum = 0
for line in contents:
    if line == "":
        inventories.append(sum)
        sum = 0
    else:
        line = line.replace('\n', '')
        sum += int(line)

max_inventory = max(inventories)

print("Part one: " + str(max_inventory))

TOP_COUNT = 3
sum = 0
for x in range(TOP_COUNT):
    max_inventory = max(inventories)
    sum += max_inventory
    inventories.remove(max_inventory)
print("Part two: " + str(sum))
