# Assignment: HW8
# File: MyStringFunctions.py
# Student: Alex Medina
# UT EID: bam5767
# Course Name: CS303E
#
# Date: 2025-10-17
# Description of Program: This program is a reimagining of many including string
#   functions for the purpose of practicing functions in Python and manipulating strings

# Usable functions
    # ord, chr
    # indexing (e.g., s[i]) and slicing (e.g., s[i:j])
    # append (i.e., ``+'')
    # len, in, not in
    # equality comparison (== or !=)) on individual characters, but not on strings
    # comparison on individual characters (<, >, <=, >=), but not on strings

def myAppend( s, ch ):
    # Return a new string that is like s but with
    # character ch added at the end
    return s + ch

def myCount( s, ch ):
    # Return the number of times character ch appears
    # in s.
    count = 0

    # loop through each letter in s
    for i in range( len( s ) ):
        # print(f"DEBUG: {i}")
        # print(f'DEBUG: {s[i]}')

        # check if letter and ch are the same
        if s[ i ] == ch:
            # print(f'DEBUG: {s[i]}')
            count += 1

    return count

def myExtend( s1, s2 ):
    # Return a new string that contains the elements of
    # s1 followed by the elements of s2, in the same
    # order they appear in s2.
    return s1 + s2

def myMin( s ):
    # Return the character in s with the lowest ASCII code.
    # If s is empty, print "Empty string: no min value"
    # and return None.

    if not s:
        print('Empty string: no min value')
        return None
    else:
        lowestASCII = ord( s[0] )
        for i in range( len(s) - 1):
            currASCII = ord( s[i+1] )
            if currASCII < lowestASCII:
                lowestASCII = currASCII
        return chr( lowestASCII )

def myInsert( s, i, ch ):
    # Return a new string like s except that ch has been
    # inserted at the ith position. I.e., the string is now
    # one character longer than before. Print "Invalid index" if
    # i is greater than the length of s and return None.

    newStr = ""

    if i > len( s ):
        print( "Invalid index" )
        return None
    else:
        for letterIndex in range( len( s ) ):
            if i == letterIndex:
                newStr += ch
            newStr += s[ letterIndex ]

        return newStr

def myPop( s, i ):
    # Return two results:
    # 1. a new string that is like s but with the ith
    #    element removed;
    # 2. the value that was removed.
    # Print "Invalid index" if i is greater than or
    # equal to len(s), and return s unchanged and None

    newStr = ""

    if i > len( s ):
        print( "Invalid index" )
        return s, None
    else:
        for letterIndex in range( len( s ) ):
            if i != letterIndex:
                newStr += s[ letterIndex ]

        return newStr, s[i]

def myFind( s, ch ):
    # Return the index of the first (leftmost) occurrence of
    # ch in s, if any. Return -1 if ch does not occur in s.

    found = -1

    for i in range( len( s ) ):
        if s[i] == ch:
            found = i
            break

    return found

def myRFind( s, ch ):
    # Return the index of the last (rightmost) occurrence of
    # ch in s, if any. Return -1 if ch does not occur in s.

    found = -1

    for i in range( len( s ) ):
        if s[i] == ch:
            found = i

    return found

def myRemove( s, ch ):
    # Return a new string with the first occurrence of ch
    # removed. If there is none, return s.

    newStr = ""
    found = False

    for i in range( len( s ) ):
        if s[i] != ch and not found:
            newStr += s[i]
        elif found:
            newStr += s[i]
        else:
            found = True

    return newStr

def myRemoveAll( s, ch ):
    # Return a new string with all occurrences of ch.
    # removed. If there are none, return s.

    newStr = ""

    for i in range(len(s)):
        if s[i] != ch:
            newStr += s[i]

    return newStr

def myEqual( s1, s2 ):
    # Return a Boolean indicating whether the input strings s1 and s2 are
    # equal.  Don't use == or is on the strings; you can use them on
    # individual characters.

    if len( s1 ) != len( s2 ):
        return False
    else:
        for i in range( len( s1) ):
            if s1[i] != s2[i]:
                return False
        return True

def myIsdigit( s ):
    # Return a Boolean indicating whether the input string s
    # is nonempty and consists only of decimal digits '0', '1', ..., '9'

    # if s is empty
    if not s:
        return False
    else:
        for i in range( len( s ) ):
            if not (s[i] == '0' or
                    s[i] == '1' or
                    s[i] == '2' or
                    s[i] == '3' or
                    s[i] == '4' or
                    s[i] == '5' or
                    s[i] == '6' or
                    s[i] == '7' or
                    s[i] == '8' or
                    s[i] == '9'):
                return False
        return True

def myReverse( s ):
    # Return a new string like s but with the characters
    # in the reverse order. For this one, don't use slicing,
    # including [::-1].

    newStr = ""

    for i in reversed( range( len( s ) ) ):
        # print(f"DEBUG: {i}")
        newStr += s[i]

    return newStr

def isPalindrome( s ):
    # Return a Boolean indicating whether the input string s
    # reads the same forward or backward. Case matters: Aba isn't
    # a palindrome.

    backwards = myReverse( s )

    return myEqual(s, backwards)

def main():
    s1 = 'Hello'
    s2 = 'l'
    print(isPalindrome("abcdeabcde"))

# main()