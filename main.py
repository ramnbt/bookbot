from stats import get_num_words
from stats import character_count
from stats import sorted_list
import sys



def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents



def main():

    #print(f"{get_num_words(frankenstein_text)} words found in the document")
    #print(character_count(frankenstein_text))
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    book_dict = character_count(book_text)
    sorted_dict_list = sorted_list(book_dict)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book_text)} total words")
    print("--------- Character Count -------")
    for entries in sorted_dict_list:
        if entries["char"].isalpha() == True:
            print(f"{entries["char"]}: {entries["num"]}")
    print("============= END ===============")
    

main()
