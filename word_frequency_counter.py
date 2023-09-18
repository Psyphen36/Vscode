from collections import Counter
import string

def word_frequency_counter(filename):
    with open(filename, 'r') as file:
        # Read the file and remove punctuation
        text = file.read().lower()
        text = text.translate(str.maketrans('', '', string.punctuation))

        # Split the text into words
        words = text.split()

        # Count the frequency of each word
        word_counts = Counter(words)

        # Get the most common words
        most_common = word_counts.most_common(10)  # Change the number to display more or fewer words

        # Display the most common words and their frequencies
        for word, count in most_common:
            print(f"{word}:- {count}")

# Example usage
filename = 'text.txt'  # Replace with your own file name
word_frequency_counter(filename)


















# from collections import Counter
# import string


# def wfc(filename):
#     with open(filename,'r') as file:
#         text = file.read().lower()
#         text = text.translate(str.maketrans('','',string.punctuation))

#         words = text.split()

#         words_count = Counter(words)

#         most_common = words_count.most_common(10)

#         for word, count in most_common:
#             print(f'{word} = {count}')

# filename = 'text.txt'
# wfc(filename)

