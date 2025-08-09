def word_count(book):
    words = book.split()
    num_words = len(words)
    return num_words

def character_count(book):
    lowercase_book = book.lower()
    char_count = {}
    for char in lowercase_book:
        if char in char_count:
            char_count[char] +=1
        else:
            char_count[char] = 1
    return char_count

def sort_on(items):
    return items["num"]

def character_sort(book):
    book_dict = character_count(book)
    new_dict = []
    for item in book_dict:
        new_item = {"char" : item, "num": book_dict[item]}
        new_dict.append(new_item)
    new_dict.sort(reverse=True, key=sort_on )
    return new_dict
