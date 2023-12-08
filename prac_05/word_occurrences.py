"""

Word Occurrences
Estimate: 25 minutes
Actual:   28 minutes

"""


def count_word_occurrences(input_string):
    word_counts = {}

    for word in input_string.split():
        word = word.strip('.,!?()[]{}"\'').lower()

        if word:
            word_counts[word] = word_counts.get(word, 0) + 1

    maximum_word_length = max(len(word) for word in word_counts.keys())

    for word in sorted(word_counts.keys()):
        count = word_counts[word]
        print(f"{word:{maximum_word_length}} : {count}")


user_input_text = input("Enter a text: ")

count_word_occurrences(user_input_text)
