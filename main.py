def main():
    path_to_file = "books/frankenstein.txt"

    with open(path_to_file) as file:
        file_contents = file.read()
        print_report(path_to_file, count_words(file_contents), count_letters(file_contents))

def count_words(string):
    words = string.split()
    return len(words)

def count_letters(string):
    result = {}
    for letter in string:
        letter = letter.lower()
        if letter in result:
            result[letter] += 1
        else:
            result[letter] = 1
    return result

def print_report(file, word_count, letters_count):
    sorted_letters = sort_letters_by_occ(letters_count)
    print(f"--- Begin report of {file} ---")
    print(f"{word_count} words found in the document")
    print()
    for letter in sorted_letters:
        print(f"The '{letter["letter"]}' character was found {letter["count"]} times")
    print("--- End report ---")

def sort_letters_by_occ(letters_count):
    result = []
    for letter in letters_count:
        if letter.isalpha():
            result.append({"letter": letter, "count": letters_count[letter]})
    result.sort(reverse=True, key=sort_on)
    return result

def sort_on(dict):
    return dict["count"]

main()