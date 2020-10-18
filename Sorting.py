"""
Four major sorting algorithms:
1. Monkey sort: aka bogosort, stupid sort, slowsort, permutation sort, shotgun sort. Best case: O(n). Worst case: unbounded !! n factorial, n to n power or even more!
2. Bubble sort: Famous sorting approach. O(n^2)
3. Selection sort: Easy to understand. O(n^2)
4. Merge sort:
"""

"""
1. Monkey sort's major steps. E.g to sort a deck of cards: 
   1. Throw them in the air
   2. Pick them up
   3. Check if they are sorted alreay. If yes, done. Otherwise repeat the throw again.
"""
def monkey_sort(L):
    while not is_sorted(L):  # This piece of code is just a demonstration as we need to define is_sorted function and import random library first.
        random.shuffle(L)


"""
2. Bubble sort's major steps: 
   1. Compare consecutive paris
   2. Swap elements in pair if needed, such that smaller element is first
   3. When reach end of list, start over again
   4. Stop when no more swaps have been made in the last look through.
"""
def bubble_sort(L):
    swap = False   # Initialize the swap variable as False
    while not swap:  # While loop is for doing multiple passes until no more swaps
        print('bubble sort: ' + str(L))
        swap = True   # Initialize swap varialbe as True
        for j in range(1, len(L)): # The for loop is for doing the comparions, indexes starting from 1 to len(L) because we always check the second element in paris.
            if L[j-1] > L[j]:  # If the first one is bigger than the second one in paris.
                swap = False   # In this case, a swap have to be made and swap variable is set as False
                temp = L[j]  # Let the second one element equal to a temprary variable
                L[j] = L[j - 1]  # Let the bigger element to the second one.
                L[j - 1] = temp  # Let the temporary element (smaller value) to the first one.

               
"""
3. Selection sort's major steps: 
   1. Compare consecutive paris
   2. Swap elements in pair if needed, such that smaller element is first
   3. When reach end of list, start over again
   4. Stop when no more swaps have been made in the last look through.
"""
def selection_sort(L):
    suffixSt = 0   # The initial position 0, i.e 1st element.
    while suffixSt != len(L):  # The loop condition until reaches the end of the list, look through the entire list
        for i in range(suffixSt, len(L)):  # Look through all elements in the list.
            if L[i] < L[suffixSt]:  # If some element is smaller than the left element
                L[suffixSt], L[i] = L[i], L[suffixSt] # Make a swap for these two values.
        suffixSt += 1  # This statement is used to go to the next for loop step.
    return L # Finanly output the result.
print(selection_sort([3, 4, 1, -8, -9]))


"""
4. Merge sort's major steps: 
   1. Compare consecutive paris
   2. Swap elements in pair if needed, such that smaller element is first.
"""
def 







