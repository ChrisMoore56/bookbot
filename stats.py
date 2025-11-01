def get_book_text(path):
    with open(path) as book:
        book_text = book.read()
        return book_text

def count_words(path):
    split_text = get_book_text(path).split()
    word_count = len(split_text)
    return word_count

def count_characters(path):
    character_count = {}
    book = get_book_text(path).lower()
    for character in book:
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    return character_count
