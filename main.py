from stats import get_num_words
from stats import get_number_characters
from stats import get_sort
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_dictionary = get_number_characters(text)
    sorted_dict = get_sort(char_dictionary)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"{num_words}")
    print("--------- Character Count -------")
    for i in sorted_dict:
        char = i["char"]
        count = i["num"]
        print(f"{char}: {count}")
    print("============= END ===============")



def get_book_text(path):
    with open(path) as f:
        return f.read()




main()