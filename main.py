def main():
    path_to_file = "books/frankenstein.txt"

    with open(path_to_file) as file:
        file_contents = file.read()
        print(file_contents)

main()