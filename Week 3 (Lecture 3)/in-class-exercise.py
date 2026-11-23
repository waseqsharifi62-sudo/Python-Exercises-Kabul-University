from collections import Counter

def word_frequency(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            words = f.read().lower().split()
        counts = Counter(words)
        for word, count in counts.most_common(10):
            print(word, count)
    except FileNotFoundError:
        pass

with open("article.txt", "w", encoding="utf-8") as f:
    f.write("This is a test article. This test is simple.")
word_frequency("article.txt")