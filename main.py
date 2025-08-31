from stats import get_num_words, get_num_char, get_sorted_char
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    text = get_book_text(book)
    num_words = get_num_words(text)
    # num_words = 75767
    num_chars = get_num_char(text)
    sorted_chars = get_sorted_char(num_chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for el in sorted_chars:
        if el["char"].isalpha():
            print(f"{el['char']}: {el['num']}")
    print("============= END ===============")

main()