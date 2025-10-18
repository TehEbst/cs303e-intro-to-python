# Assignment: HW8
# File: MyStringFunctions.py
# Student: Alex Medina
# UT EID: bam5767
# Course Name: CS303E
#
# Date: 2025-10-17
# Description of Program:

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
    pass

def myExtend( s1, s2 ):
    # Return a new string that contains the elements of
    # s1 followed by the elements of s2, in the same
    # order they appear in s2.
    pass

def myMin( s ):
    # Return the character in s with the lowest ASCII code.
    # If s is empty, print "Empty string: no min value"
    # and return None.
    pass

def myInsert( s, i, ch ):
    # Return a new string like s except that ch has been
    # inserted at the ith position. I.e., the string is now
    # one character longer than before. Print "Invalid index" if
    # i is greater than the length of s and return None.
    pass

def myPop( s, i ):
    # Return two results:
    # 1. a new string that is like s but with the ith
    #    element removed;
    # 2. the value that was removed.
    # Print "Invalid index" if i is greater than or
    # equal to len(s), and return s unchanged and None
    pass

def myFind( s, ch ):
    # Return the index of the first (leftmost) occurrence of
    # ch in s, if any. Return -1 if ch does not occur in s.
    pass

def myRFind( s, ch ):
    # Return the index of the last (rightmost) occurrence of
    # ch in s, if any. Return -1 if ch does not occur in s.
    pass

def myRemove( s, ch ):
    # Return a new string with the first occurrence of ch
    # removed. If there is none, return s.
    pass

def myRemoveAll( s, ch ):
    # Return a new string with all occurrences of ch.
    # removed. If there are none, return s.
    pass

def myEqual( s1, s2 ):
    # Return a Boolean indicating whether the input strings s1 and s2 are
    # equal.  Don't use == or is on the strings; you can use them on
    # individual characters.
    pass

def myIsdigit( s ):
    # Return a Boolean indicating whether the input string s
    # is nonempty and consists only of decimal digits '0', '1', ..., '9'
    pass

def myReverse( s ):
    # Return a new string like s but with the characters
    # in the reverse order.  For this one, don't use slicing,
    # including [::-1].
    pass

def isPalindrome( s ):
    # Return a Boolean indicating whether the input string s
    # reads the same forward or backward. Case matters: Aba isn't
    # a palindrome.
    pass

def main():
    s1 = 'Hello'
    s2 = myAppend(s1, "World")
    print( s2 )
main()