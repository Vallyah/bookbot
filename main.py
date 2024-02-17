def main():
    path_to_file = "books/frankenstein.txt"

    with open(path_to_file) as file:
        file_contents = file.read()
        print(count_words(file_contents))

def count_words(string):
    words = string.split()
    return len(words)

main()