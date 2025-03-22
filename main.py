from stats import get_number_of_words
from stats import get_number_of_characters
from stats import sort_dict 
import sys

def main():
    arg = sys.argv
    if len(arg) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_txt = get_book_text(arg[1])
        get_number_of_words(book_txt)
        #get_number_of_characters(book_txt)
        sort_dict(get_number_of_characters(book_txt))
    
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

main()

