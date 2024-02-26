def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    print_report(chars_sorted_list,num_words,book_path)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    

def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(dict):
    return dict["num"]


def print_report(chars_sorted_list,num_words,path):
    print (f"--- Begin report of {path} ---")
    print (f"{num_words} words found in the document\n\n" )
    for i in range (0,len(chars_sorted_list)):
        if not chars_sorted_list[i]["char"].isalpha():
            continue
        print(f"The '{chars_sorted_list[i]['char']}' character was found {chars_sorted_list[i]['num']} times")
    
    print("--- End report ---")


main()