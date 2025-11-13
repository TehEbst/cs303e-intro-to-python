# Assignment: HW11
# File: WordleAssistant.py
# Student: Alex Medina
# UT EID: bam5767
# Course Name: CS303E
#
# Date: 2025-11-13
# Description of Program: The purpose of this file is to create functions to
#   help with playing the game Wordle. It defines four different tools that
#   might be helpful to a wordle player as well as a function to create a
#   wordlist from a readable file.

def createWordlist(filename):
    """ Read words from the provided file and store them in a list.
    The file contains only lowercase ascii characters, are sorted
    alphabetically, one word per line. Filter out any words that are
    not 5 letters long, have duplicate letters, or end in 's'. Return
    the list of words and the number of words as a pair. """

    # Some helper functions to help filter the list
    def tooLong(s):
        # Return true if word is 5 letters long
        return len(s) == 5
    def noDupLetters(s):
        # Return true if there are no duplicate letters in s
        return len(s) == len(set(s))
    def noEndS(s):
        # Return true if string does not end in s
        return not s.endswith('s')

    # Open the file in read mode, which is the default, but I specified
    rawWordList = open(filename, 'r')
    wordList = rawWordList.readlines()

    # Remove the escape character and white space from each string
    for i, word in enumerate(wordList):
        wordList[i] = word.strip()

    # Run two filters to only include 5 letter words and no double letters
    wordList = list(filter(tooLong, wordList))
    wordList = list(filter(noDupLetters, wordList))
    # One last filter to remove words that end in 's'
    wordList = list(filter(noEndS, wordList))

    return wordList, len(wordList)

def containsAll(wordlist, include):
    """ Given your wordlist, return a set of all words from the wordlist
    that contain all of the letters in the string include.
    """

    for ch in include:
        wordlist = {word for word in wordlist if ch in word}

    return wordlist

def containsNone(wordlist, exclude):
    """ Given your wordlist, return a set of all words from the wordlist
    that do not contain any of the letters in the string exclude.
    """

    for ch in exclude:
        wordlist = {word for word in wordlist if ch not in word}

    return wordlist

def containsAtPositions(wordlist, posInfo):
    """ posInfo is a dictionary that maps letters to positions.
    You can assume that the positions are in [0..4]. Return a set of
    all words from the wordlist that contain the letters from the
    dictionary at the indicated positions. For example, given posInfo
    {'a': 0, 'y': 4}.  This function might return the set:
    {'angry', 'aptly', 'amply', 'amity', 'artsy', 'agony'}. """

    # For each dictionary entry
    for key, value in posInfo.items():
        # Honestly, I am so proud of writing this set (list) comprehension
        # Basically, for each word in the entire wordlist, we check if key,
        # which is the letter, occurs at the appropriate value, which is the
        # position, in the word in wordlist
        wordlist = {word for word in wordlist if key in word[value]}

    return wordlist

def getPossibleWords(wordlist, posInfo, include, exclude):
    """ Finally, given a wordlist, dictionary posInfo, and
    strings include and exclude, return the set of all words from
    the wordlist that contains the words that satisfy all of
    the following:
    * has letters in positions indicated in posInfo
    * contains all letters from string include
    * contains none of the letters from string exclude.
    """

    wordlist = containsAll(wordlist, include)
    wordlist = containsNone(wordlist, exclude)
    wordlist = containsAtPositions(wordlist, posInfo)
    return wordlist

def main():
    # When using a file name, our program can only see files within its
    # current folder. It reads from left to right. The ".." specifies that
    # it needs to move up one folder
    filename = "../resources/new-wordlist.txt"
    s = createWordlist(filename)

    print(getPossibleWords( s[0], {'a':0, 'b':1}, "o", "v" ))

# main()

