import sys
from stats import book_word_count, character_count, dict_split

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    word_count = book_word_count(book_text)
    char_dict = character_count(book_text)
    char_count = dict_split(char_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in char_count:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


main()