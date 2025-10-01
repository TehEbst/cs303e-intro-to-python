# CS 303E Quiz 1C
# do NOT rename this file, otherwise Gradescope will not accept your submission


# Problem 1: Clothing Purchases
def clothingPurchases():
    # Define constants which are the prices of each item
    TSHIRT = 19.98
    JEANS = 33.95
    COLOGNE = 74.95
    BELT = 48.72
    PERFUME = 81.81

    # Total price
    totalPrice = TSHIRT + JEANS + COLOGNE + BELT + PERFUME

    # Get user input for which two items are sold out
    soldOutItem1 = input()
    soldOutItem2 = input()

    # Calculate total cost minus the two items that are sold out
    for item in [soldOutItem1, soldOutItem2]:
        if item == 'T-Shirt':
            totalPrice -= TSHIRT
        elif item == 'Jeans':
            totalPrice -= JEANS
        elif item == 'Cologne':
            totalPrice -= COLOGNE
        elif item == 'Belt':
            totalPrice -= BELT
        elif item == 'Perfume':
            totalPrice -= PERFUME

    # Display output
    print(f'${totalPrice:.2f}')
    pass


# Problem 2: First Term Larger than k
def firstTermLarger():
    # Read in a positive float k
    k = float(input())
    n = 1
    a = 0

    # Find the smallest term in the sequence whose value is larger than k
    while k > a:
        a = (.65 * n**2) + (1.32 * n)
        n += 1

    # Print smallest term to 2 decimal places
    print(f'{a:.2f}')
    pass


if __name__=="__main__":
    """
    If you want to test your code on your computer, uncomment the respective
    function call(s) below.
    
    DO NOT CALL YOUR FUNCTIONS ANYWHERE OUTSIDE OF THIS AREA
    """
    # clothingPurchases()
    # firstTermLarger()

    # DO NOT DELETE THIS PASS
    pass
    # DON'T DO IT