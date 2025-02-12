def findLongestWord(listToAnalize): 
    longWordList = 0; targetIndex = 0
    for i in listToAnalize: 
        if len(i) > longWordList: targetIndex = i; longWordList = len(i)
    return targetIndex
userInput = input("Insert some text"); print("The longest word is: " + findLongestWord(userInput.split()))