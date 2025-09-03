def get_num_words(book_text):
    num_words = len(book_text.split())
    return num_words

def character_count(book_text):
    return_dict = {}
    for i in range(len(book_text)):
        return_dict[book_text[i].lower()]  = 0
    for i in range(len(book_text)):
        return_dict[book_text[i].lower()]+= 1

    return return_dict

    
        