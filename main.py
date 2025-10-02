
from stats import get_num_words , get_num_characters, report

def get_text_book():
    with open("books/frankenstein.txt", "r") as file:
        text = file.read()

    return text

def main():
    text = get_text_book()
    total_words = get_num_words(text)
    chars = get_num_characters(text)
    report(chars,total_words)

main()