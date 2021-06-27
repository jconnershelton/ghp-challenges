'''
You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each 
character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

 

Example 1:

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3

Example 2:

Input: jewels = "z", stones = "ZZ"
Output: 0
'''
# Aryan Mittal's Solution
def numJewelsInStones(jewels, stones):
    """
    :type jewels: str
    :type stones: str
    :rtype: int
    """
    #O(n+k) = O(n)
    count = 0
    jewels = set(jewels) #O(n)
    for stone in stones: # O(k)
        if stone in jewels: #O(1)
            count += 1

    return count