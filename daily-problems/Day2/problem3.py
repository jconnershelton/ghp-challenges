'''
We define str = [s, n] as the string str which consists of the string s concatenated n times.

For example, str == ["abc", 3] =="abcabcabc".
We define that string s1 can be obtained from string s2 if we can remove some characters from s2 such that it becomes s1.

For example, s1 = "abc" can be obtained from s2 = "abdbec" based on our definition by removing the bolded underlined characters.
You are given two strings s1 and s2 and two integers n1 and n2. You have the two strings str1 = [s1, n1] and str2 = [s2, n2].

Return the maximum integer m such that str = [str2, m] can be obtained from str1.

 

Example 1:

Input: s1 = "acb", n1 = 4, s2 = "ab", n2 = 2
Output: 2

Example 2:

Input: s1 = "acb", n1 = 1, s2 = "acb", n2 = 1
Output: 1
'''
# Aryan Mittal's Solution
def getMaxRepetitions(s1, n1, s2, n2):
    """
    :type s1: str
    :type n1: int
    :type s2: str
    :type n2: int
    :rtype: int
    """
    # a = s1 * n1, b = s2 * n2
    # overall complexity is O(a × b^2), wrt a and b
    str1 = list(s1 * n1) #O(a)
    str2 = list(s2 * n2) #O(b)

    count = 0
    i = 0
    while i < len(str2): #O(b)
        if (char := str2[i]) in str1: #O(a)
            str1.remove(char) #O(a)
            str2.remove(char) #O(b)
        else:
            i += 1 #O(1)
        if not str2: #O(1)
            count += 1 #O(1)
            str2 = list(s2 * n2) #O(b)

    return count

