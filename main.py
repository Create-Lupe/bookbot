from stats import count_words, count_characters,sort_characters_by_count
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()


def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    book_text = get_book_text(book_path)

    print("----------- Word Count ----------")
    num_words = count_words(book_text)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    char_counts = count_characters(book_text)
    sorted_chars = sort_characters_by_count(char_counts)

    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

    


if __name__ == "__main__":
    main()