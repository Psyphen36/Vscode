def count_words(text):
    words = text.split()
    word_count = len(words)
    return word_count

def main():
    text = input("Enter a text: ")
    count = count_words(text)
    print("Word count:", count)

if __name__ == "__main__":
    main()

