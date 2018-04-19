import sys

filename = sys.argv[1]
freq = {}
for piece in open(filename).read().lower().split():
    # only consider alphabetic characters within this piece
    word = ''.join(c for c in piece if c.isalpha())
    if word:  # require at least one alphabetic character
        freq[word] = 1 + freq.get(word, 0)
max_word = ''
max_count = 0
for (w, c) in freq.items():  # (key, value) tuples represent (word, count)
    if c > max_count:
        max_word = w
        max_count = c
print('The most frequent word is', max_word)
print('Its number of occurrences is', max_count)
