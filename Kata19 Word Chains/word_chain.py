def setupDictionary(words) :
    upperWords = list()
    for word in words :
        upperWords.append(word.upper().strip('\n'))
    return tuple(upperWords)

def NeighbourWords(word) :
    neighbours = []
    # for every letter
    wordLength = len(word)
    for letter in range(0, wordLength) :
        splitWord = list(word)
        # change this letter to something else
        for c in range(ord('A'), ord('Z') + 1) :
            alphaCaracter = chr(c)
            #print(alphaCaracter)
            if alphaCaracter != word[letter] :
              #print(alphaCaracter)
              splitWord[letter] = alphaCaracter
              #print(splitWord)
              neighbours.append("".join(splitWord))
    #print(neighbours)
    #print(len(neighbours))
    return neighbours

def findWordsChain(startWord, stopWord, dictionary) :
    startWord = startWord.upper() 
    stopWord = stopWord.upper()
    chain = list()
    visitedWords = set()
    backtrack = dict()

    chain.append(startWord)
    visitedWords.add(startWord)

    while len(chain) > 0 :
        firstWord = chain.pop(0)
        #print(firstWord)
        # for each neighbour of first word
        for neighbour in NeighbourWords(firstWord) :
            if neighbour == stopWord :
                # word found, backtrack
                pruneChain = [neighbour]
                #print(pruneChain)
                while len(firstWord) > 0 :
                    pruneChain.insert(0, firstWord)
                    if firstWord in backtrack :
                        firstWord = backtrack[firstWord]
                    else :
                        firstWord = ""
                return pruneChain

            if neighbour in dictionary :
                if not neighbour in visitedWords :
                    chain.append(neighbour)
                    #print(chain)
                    #mark visited
                    visitedWords.add(neighbour)
                    backtrack[neighbour] = firstWord
                    #print(backtrack)

fileName = "simpleDictionary.txt"
file = open(fileName,"r")
words = file.readlines()
file.close()
dictionary = setupDictionary(words)

#test and call the function
wordschain = findWordsChain("cat", "tan", dictionary)

print(wordschain)

