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

#def add_num_key(dictionary):
 #   num_dictionary = dictionary
  #  for item in dictionary:
   #     num_dictionary["num"] = dictionary[item]
    #print (num_dictionary)

def sort_on(items):
    return items["num"]



def character_report(path):
    character_dictionary = count_characters(path)
    key_list = character_dictionary.keys()
    char_list = []

    for key in key_list:
        if key.isalpha():
            char_list.append({"char": key, "num": character_dictionary[key]})

    char_list.sort(reverse=True, key=sort_on)

    return char_list
