

def word_count(book_text):
    words = book_text.split()
    return len(words)

def char_count(book_text):

    full_count = {}

    lower_count = book_text.lower()
    for char in lower_count:
        if char in full_count:
            full_count[char] += 1
        else:
            full_count[char] = 1

    return full_count

def sort_on(dict):
    return dict["num"]

def sorted_char(full_count):
    sorted_count = []
    for i in full_count:
        char_list = {"char": i, "num": full_count[i]}
        sorted_count.append(char_list)
    sorted_count.sort(reverse=True, key=sort_on)
    return sorted_count