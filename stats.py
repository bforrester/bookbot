def wordCount(content):
    words = content.split()
    return len(words)


def charactersCount(content):
    contentLower = content.lower()
    characters = {}
    words = contentLower.split()
    for word in words:
        for i in range(len(word)):
            letter = word[i]
            if letter in characters:
                characters[letter] = characters[letter] + 1
            else:
                characters[letter] = 1
    return characters

                
def printReport(charDict: dict[str, int], wordCount):
    # print(charDict)
    charList = []

    for char, count in charDict.items():
        
        charList.append({"char": char, "count": count})

        def sort_on(dict_item):
            return dict_item["count"]
        
        charList.sort(reverse=True, key=sort_on)
        

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {wordCount} total words")
    print("--------- Character Count -------")
    for item in charList:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["count"]}")
    print("============= END ===============")


