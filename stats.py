def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    counts = {}
    for char in text:
        lower_char = char.lower()
        counts[lower_char] = counts.get(lower_char, 0) + 1
    return counts

def sort_chars_by_count(char_dict):
    chars_list = []

    for char, count in char_dict.items():
        char_info = {"character": char, "count": count}
        chars_list.append(char_info)

    def sort_on(dict_item):
        return dict_item["count"]

    chars_list.sort(reverse=True, key=sort_on)

    return chars_list
