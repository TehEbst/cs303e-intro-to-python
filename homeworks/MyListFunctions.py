# Assignment: HW9
# File: MyListFunctions.py
# Student: Alex Medina
# UT EID: bam5767
# Course Name: CS303E
#
# Date: 2025-10-21
# Description of Program: For the purposes of learning Python, this file
#   contains an assortment of basic list manipulation functions. Using only
#   very basic default functions, this file aims to recreate many more
#   advanced list manipulation functions

# Assignment Link:
#   https://www.cs.utexas.edu/~byoung/cs303e/hw9.html

# The only list functions/methods you can use in this assignment are:
#   indexing (e.g., lst[i] but not .index()) and slicing (e.g., lst[i:j],
#       except no slicing for mySlice)
#   append (i.e., ``+'')
#   len, in, not in
#   equality comparison on individual elements, but not on lists (== or !=))

def myAppend( lst, x ):
    # Return a new list that is like lst but with
    # the element x at the right end
    return lst + [x]

def myExtend( lst1, lst2 ):
    # Return a new list that contains the elements of
    # lst1 followed by the elements of lst2 in the order
    # given.
    return lst1 + lst2

def myMax( lst ):
    # Return the element with the highest value.
    # If lst is empty, print "Empty list: no max value"
    # and return None.  You can assume that the list
    # elements can be compared.

    if not lst:
        print('Empty list: no max value')
        return None
    else:
        maxVal = lst[0]

        for i in range(len(lst) - 1):
            # print(f'DEBUG: {i}')
            if lst[i + 1] > maxVal:
                maxVal = lst[i + 1]

        return maxVal

def mySum( lst ):
    # Return the sum of the elements in lst.  Assume
    # that the elements are numbers.
    sum = 0

    for i in range( len(lst) ):
        sum += lst[i]

    return sum

def myCount( lst, x ):
    # Return the number of times element x appears
    # in lst.
    numX = 0

    for i in range( len(lst) ):
        if lst[i] == x:
            numX += 1

    return numX

def myInsert( lst, i, x ):
    # Return a new list like lst except that x has been
    # inserted at the ith position.  I.e., the list is now
    # one element longer than before. Print "Invalid index" if
    # i is negative or is greater than the length of lst and
    # return None.
    lst2 = []

    if i > len(lst) or i < 0:
        print('Invalid index')
        return None

    for j in range( len(lst) ):
        if i == j:
            lst2 += [x]
        lst2 += [lst[j]]

    return lst2

def myPop( lst, i ):
    # Return two results:
    # 1. a new list that is like lst but with the ith
    #    element removed;
    # 2. the value that was removed.
    # Print "Invalid index" if i is negative or is greater than
    # or equal to len(lst), and return lst unchanged, and None
    lst2 = []
    pop = None

    if i < 0 or i >= len(lst):
        print('Invalid index')
        lst2 = lst
    else:
        for j in range( len(lst) ):
            if j == i:
                pop = lst[j]
                continue
            lst2 += [lst[j]]

    return lst2, pop

def myFind( lst, x ):
    # Return the index of the first (leftmost) occurrence of
    # x in lst, if any.  Return -1 if x does not occur in lst.
    idx = -1

    for i in range( len(lst) ):
        if lst[i] == x:
            idx = i
            break

    return idx

def myRFind( lst, x ):
    # Return the index of the last (rightmost) occurrence of
    # x in lst, if any.  Return -1 if ch does not occur in lst.
    idx = -1

    for i in reversed( range( len(lst) ) ):
        if lst[i] == x:
            idx = i
            break

    return idx

def myFindAll( lst, x ):
    # Return a list of indices of occurrences of x in lst, if any.
    # Return the empty list if there are none.
    lst2 = []

    for i in range( len(lst) ):
        if lst[i] == x:
            lst2 = myAppend(lst2, i)

    return lst2

def myReverse( lst ):
    # Return a new list like lst but with the elements
    # in the reverse order.
    lst2 = []

    for i in reversed( range( len(lst) ) ):
        lst2 += [lst[i]]

    return lst2

def myRemove( lst, x ):
    # Return a new list with the first occurrence of x
    # removed.  If there is none, return lst.
    if x in lst:
        idx = myFind(lst, x)
        return myPop(lst, idx)[0]
    else:
        return lst

def myRemoveAll( lst, x ):
    # Return a new list with all occurrences of x
    # removed.  If there are none, return lst.
    allRemoved = False

    while not allRemoved:
        if x in lst:
            lst = myRemove(lst, x)
        else:
            allRemoved = True

    return lst

def myEqual( lst1, lst2 ):
    # Return a Boolean indicating whether the input lists lst1 and lst2 are
    # equal.  Don't use == on the lists; you can use them on
    # individual elements.  Make sure to check that the lengths are equal.
    if len(lst1) != len(lst2):
        return False
    else:
        for i in range( len(lst1) ):
            if lst1[i] != lst2[i]:
                return False
        return True

def allEqual( lst, x ):
    # Return a Boolean indicating whether in list lst all elements, if
    # any, are equal to x.
    if not lst:
        return True
    elif x not in lst:
        return False
    else:
        for i in range( len(lst) ):
            if lst[i] != x:
                return False
        return True

# Don't use slicing for this one:
def mySlice( lst, i, j ):
    # A limited version of the slice operations on lists.
    # If i and j are in [0..len(lst)], return the list
    # [ lst[i], lst[i+1], ... lst[j-1] ].  I.e.,
    # the slice lst[i:j].  Print an error message if either
    # i or j is not in [0..len(lst)].  Notice that this is
    # similar but not identical to the way Python slice behaves.
    if not (0 <= i <= len(lst)
            and 0 <= j <= len(lst)):
            # and j >= i):
        print('Illegal index value')
    else:
        lst2 = []

        for k in range(i, j):
            lst2 += [lst[k]]

        return lst2

def orderedListOfNumbers( lst ):
    # Assume lst is a list of floats.  Return a Boolean indicating all
    # elements (if any) are in ascending order.  It's OK if two successive
    # elements are equal.
    ascending = True

    for i in range( len(lst) - 1):
        # print(f'DEBUG: {i}')
        if lst[i] > lst[i + 1]:
            ascending = False
            break

    return ascending

def main():
    lst1 = [1, 2, 3, 1]
    lst2 = [4, 5, 6]
    lst3 = allEqual([], [])
    print(lst3)

# main()