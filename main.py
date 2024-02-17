def main():
    path_to_file = "books/frankenstein.txt"

    with open(path_to_file) as file:
        file_contents = file.read()
        print(count_letters(file_contents))

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

main()