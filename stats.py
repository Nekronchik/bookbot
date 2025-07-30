def get_num_words(text):
    splitted_text = text.split()
    count_word = len(splitted_text)
    return f"Found {count_word} total words"


def get_number_characters(text):
    lower_text = text.lower()
    char_count = {}
    for char in lower_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1 
    return char_count


def sort_on(item):
    return item["num"]


def get_sort(chars_dict):
    result = []
    for char in chars_dict:
        if char.isalpha():
            count = chars_dict[char]
            char_info = {"char": char, "num": count}
            result.append(char_info)
    result.sort(reverse=True, key=sort_on)
    return result
