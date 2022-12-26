from collections import Counter
some_words = """apple orange  pinapple, melon strawberry orange apple blueberry pinapple apple corn 
                strawberry pinapple orange apple melon strawberry  orange 
                apple blueberry pinapple corn strawberry pinapple orange"""
split_words = some_words.split()
count_words = Counter(split_words)
max_val = max(count_words.values())


def get_word(count_words, value):
    for k, v in reversed(count_words.items()):
        if v == value:
            return k


print(f"Most popular word in string is {get_word(count_words, value=max_val)} , it occurs {max_val} times ")
