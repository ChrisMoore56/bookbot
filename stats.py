def get_book_text(path):
    with open(path) as book:
        book_text = book.read()
        return book_text

def count_words(path):
    split_text = get_book_text(path).split()
    word_count = len(split_text)
    return word_count
