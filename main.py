
import sys
from stats import get_num_words , get_num_characters, total_chars

def get_text_book():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)  # Exit program with status code 1

    # The second argument is the book path
    book_path = sys.argv[1]
    print(f"Reading book from: {book_path}")

    with open(book_path, "r") as file:
        text = file.read()

    return text

def main():
    text = get_text_book()
    total_words = get_num_words(text)
    chars = get_num_characters(text)
    list = total_chars(chars)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for key in list:
        if key["char"].isalpha():
            print(f"{key["char"]}: {key["num"]}")
    print("============= END ===============")

    print(sys.argv)

main()