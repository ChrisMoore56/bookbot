from stats import get_book_text, count_words

def main():
    path = "./books/frankenstein.txt"
    word_count = count_words(path)
    message = f"Found {word_count} total words"
    print(message)

main()