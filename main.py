from stats import word_count, character_count, character_sort
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def print_report(book_path, word_count, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    # Use a regular for loop, not inside a print statement
    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    
    print("============= END ===============")

def main():
    book_path = ""
    if len(sys.argv) > 1:
        book_path = sys.argv[1]
    else: 
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(book_path)
    
    wc = word_count(text)           # Get word count
    char_sort = character_sort(text) # Get sorted character list
    
    print_report(book_path, wc, char_sort)  # Pass the sorted list, not the dict

if __name__ == "__main__":
    main()