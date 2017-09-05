def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    count=1
    for i in secretWord:
        if count<len(secretWord) and i in lettersGuessed:
            count+=1
        elif count==len(secretWord) and i in lettersGuessed:
            return True
        else:
            return False
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    showString=''
    showList=[]
    for i in secretWord:
        showList.append('_') 
    i=0
    for i in range(0,len(secretWord)):
        if secretWord[i] in lettersGuessed:
            showList[i]=secretWord[i]
    for k in showList:
        showString=showString+k
    return showString
            
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    string=''
    refList=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in lettersGuessed:
        refList.remove(i)
    i=0
    for i in refList:
        string=string+i
    return string
        
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    lettersGuessed=[]
    print 'Welcome to the game, Hangman!'
    print''
    print'I am thinking of a word that is '+str(len(secretWord))+' letters long.'
    print('_ _ _ _ _ _ _ _ _ _ _ _ _')
    guesses=8
    while getGuessedWord(secretWord,lettersGuessed)!=secretWord and guesses>0:
        print 'You have '+str(guesses)+'guesses left.'
        print ''
        print 'Available Letters: '+getAvailableLetters(lettersGuessed)
        print ''
        input1=raw_input('Please guess a letter: ')
        input2=input1.lower()
        print ''
        if input2 in lettersGuessed:
            print "Oops! You've already guessed that letter: "+getGuessedWord(secretWord,lettersGuessed)
            print('_ _ _ _ _ _ _ _ _ _ _ _')
        elif input2 in secretWord:
            lettersGuessed.append(input2)
            print 'Good guess: '+getGuessedWord(secretWord,lettersGuessed)
            print('_ _ _ _ _ _ _ _ _ _ _ _')
        else:
            lettersGuessed.append(input2)
            print 'Oops! That letter is not in my word: '+getGuessedWord(secretWord,lettersGuessed)
            guesses-=1
            print('_ _ _ _ _ _ _ _ _ _ _ _')
    if isWordGuessed(secretWord, lettersGuessed)==True:
        print 'Congratulations, you won!'
    else:
        print 'Sorry, you ran out of guesses. The word was '+secretWord
