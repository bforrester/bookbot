from stats import wordCount, charactersCount, printReport
import sys 
import os.path

def main():
    # filePath = "./books/frankenstein.txt"
    if len(sys.argv) != 1:
        filepath = sys.argv[1]
        if os.path.isfile(filepath):
            content = get_book_text(filepath)
            count = wordCount(content)
            chars = charactersCount(content)
            printReport(chars, wordCount(content))
        else:
            sys.exit(1)

    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # print(f"{count} words found in the document")



def get_book_text(filePath):
    with open(filePath) as f:
        fileContents = f.read()
        return fileContents



main()