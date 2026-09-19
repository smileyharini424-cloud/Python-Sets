set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Set 1:", set1)
print("Set 2:", set2)

set1.add(7)
print("After Add:", set1)

set1.remove(7)
print("After Remove:", set1)

print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference:", set1.difference(set2))
