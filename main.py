
from stats import get_num_words , get_num_characters, total_chars

def get_text_book():
    with open("books/frankenstein.txt", "r") as file:
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

main()