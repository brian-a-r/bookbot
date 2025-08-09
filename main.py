from stats import word_count, character_count

def get_book_text(filepath):
    with open(filepath) as f:
        book_contents = f.read()
        print(book_contents)
    return book_contents


def main():
    get_book_text("books/frankenstein.txt")
    word_count(get_book_text("books/frankenstein.txt"))  
    character_count(get_book_text("books/frankenstein.txt")) 

if __name__ == "__main__":
    main()