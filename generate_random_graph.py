from string import ascii_lowercase
import random

letters = list(ascii_lowercase)
occurrences = []
f = open("random_edges.txt", "w+")
for i in range(1, 60):
    x = random.choice(letters)
    y = random.choice(letters)
    xy = ''.join([x, y])
    if x != y and xy not in occurrences:
        occurrences.append(xy)
        f.write('%c %c\n' % (x, y))
f.close()