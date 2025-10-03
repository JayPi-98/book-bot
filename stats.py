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

def sort_on(items):
    return items["num"]

def total_chars(chars):
    char_list = []

    for c in chars:
        entry = {"char": "", "num": 0}
        entry["char"] = c
        entry["num"] = chars[c]
        char_list.append(entry)
    char_list.sort(reverse=True, key=sort_on)

    return char_list

