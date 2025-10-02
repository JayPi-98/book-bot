def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def report(chars, total_words):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for c in sorted(chars):
        if c.isalpha():
            print(f"'{c}': {chars[c]}")
    print("============= END ===============")

