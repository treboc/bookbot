def main():
    with open("books/frankenstein.txt") as f:
        filestring = f.read()
        dict = make_count_char_dict(filestring)
        converted_list = convert_to_list(dict)
        counted_words = count_words(filestring)
        print_report(counted_words, converted_list)


def count_words(filestring):
    words = filestring.split()
    return len(words)


def make_count_char_dict(filestring) -> dict:
    lower = filestring.lower()
    dict = {}

    for char in lower:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1

    return dict


def convert_to_list(dict) -> list:
    list = []
    for k in dict:
        if k.isalpha():
            foo = {"char": k, "count": dict[k]}
            list.append(foo)

    list.sort(key=sort_on, reverse=True)
    return list


def sort_on(dict):
    return dict["count"]


def print_report(counted_words, counted_chars_list):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{counted_words} words found in the document")

    for item in counted_chars_list:
        print(
            f"The {item['char']} character was found {item['count']} times in the document."
        )

    print("--- End Report ---")


main()
