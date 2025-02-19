def findLongestWord(listToAnalize, longWordList, targetWord):
    for word in listToAnalize: 
        if len(word) > longWordList: targetWord = word; longWordList = len(word)
    return targetWord
userInput = input("Insert some text"); print("The longest word is: " + findLongestWord(userInput.split(), 0, 0))