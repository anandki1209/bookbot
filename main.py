from stats import get_num_words
from stats import count_occurence
from stats import sort_dict

import sys


def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    content = get_book_text(file_path)
    num_words = get_num_words(content)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")


    num_of_repeats = count_occurence(content)
    sorted_list = sort_dict(num_of_repeats)
    for item  in sorted_list:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    
    print("============= END ===============")








def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()   
    



main() 





