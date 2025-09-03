from stats import get_num_words
from stats import character_count
def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

frankenstein_text = get_book_text("./books/frankenstein.txt")

def main():
    print(f"{get_num_words(frankenstein_text)} words found in the document")
    print(character_count(frankenstein_text))

main()
