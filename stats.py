def word_count(book):
    words = book.split()
    num_words = len(words)
    print(f"{num_words} words found in the document")

def character_count(book):
    lowercase_book = book.lower()
    char_count = {}
    for char in lowercase_book:
        if char in char_count:
            char_count[char] +=1
        else:
            char_count[char] = 1
    print(char_count)
