import sys

def get_book_text(file_path):
    with open(file_path) as f:
        book_text = f.read()
    return book_text

from stats import word_count, char_count, sorted_char

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    num_words = word_count(book_text)
    print(f"Found {num_words} total words")
    char_counts = char_count(book_text)
    sorted_counts = sorted_char(char_counts)
    print(char_counts)
    for l in sorted_counts:
        character = l["char"]
        count = l["num"]
        if not character.isalpha():
            continue
        print(f"{character}: {count}")


if __name__ == "__main__":
    main()