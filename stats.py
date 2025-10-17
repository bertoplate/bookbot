def book_word_count(text):
    words = len(text.split())
    return words

def character_count(text):
    lowercase = text.lower()
    character_dict = {}
    for character in lowercase:
        if character.isalpha():
            if character in character_dict:
                character_dict[character] += 1
            else:
                character_dict[character] = 1
    return character_dict

def dict_split(dicts):
    dict_list = []
    for char, num in dicts.items():
        char_dict = {"char": char, "num": num}
        dict_list.append(char_dict)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

def sort_on(item):
    return item["num"]