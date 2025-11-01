from stats import get_book_text, count_words, count_characters

def main():
    path = "./books/frankenstein.txt"
    
    word_count = count_words(path)
    message = f"Found {word_count} total words"
    print(message)

    print(count_characters(path))

main()