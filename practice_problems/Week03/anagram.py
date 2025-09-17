anagrams = [
    "tap", "pat",
    "ate", "tea",
    "god", "dog",
    "rat", "tar",
    "tops", "stop"
    "car", "apt"
]

d = {}

for word in anagrams:
    if tuple(sorted(word)) in d:
        d[ tuple(sorted(word)) ].append(word)
    else:
        d[ tuple(sorted(word)) ] = [word]

print(d[('a', 'p', 't')][0])