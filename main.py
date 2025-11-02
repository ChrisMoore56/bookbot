from stats import get_book_text, count_words, count_characters, character_report
import sys

def main():
    #path = "books/frankenstein.txt"
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]

    
    word_count = count_words(path)
    message = f"Found {word_count} total words"
    #print(message)

    #print(count_characters(path))
    #print(character_report(path))

    report_data = character_report(path)
    print(f"============ BOOKBOT ============\nAnalyzing book found at {path}\n----------- Word Count ----------\n{message}\n--------- Character Count -------")
    for dictionary in report_data:
        print(f"{dictionary["char"]}: {dictionary["num"]}")
    print("============= END ===============")

main()