def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_counts = {}
    for char in text.lower():  # Normalize to lowercase
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_characters_by_count(char_counts):
    # Step 1: Convert to list of dictionaries
    char_list = []
    for char, count in char_counts.items():
        if char.isalpha():  # Only include alphabetic characters
            char_list.append({"char": char, "num": count})

    # Step 2: Define helper function for sorting
    def get_count(item):
        return item["num"]

    # Step 3: Sort the list in descending order
    char_list.sort(key=get_count, reverse=True)

    return char_list
