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

def sort_on(items):
    return items["num"]

def sorted_list(dict):
    dicts_list = []
    for key in dict:
        new_dict = {}
        new_dict["char"] = key
        new_dict["num"] = dict[key]
        dicts_list.append(new_dict)
    dicts_list.sort(reverse=True, key=sort_on)
    return dicts_list
        