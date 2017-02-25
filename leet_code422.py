"""
422. Valid Word Square

Given a sequence of words, check whether it forms a valid word square.

A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 <= k < max(numRows, numColumns).

Note:
The number of words given is at least 1 and does not exceed 500.
Word length will be at least 1 and does not exceed 500.
Each word contains only lowercase English alphabet a-z.
Example 1:

Input:
[
  "abcd",
  "bnrt",
  "crmy",
  "dtye"
]

Output:
true

Explanation:
The first row and first column both read "abcd".
The second row and second column both read "bnrt".
The third row and third column both read "crmy".
The fourth row and fourth column both read "dtye".

Therefore, it is a valid word square.
Example 2:

Input:
[
  "abcd",
  "bnrt",
  "crm",
  "dt"
]

Output:
true

Explanation:
The first row and first column both read "abcd".
The second row and second column both read "bnrt".
The third row and third column both read "crm".
The fourth row and fourth column both read "dt".

Therefore, it is a valid word square.
Example 3:

Input:
[
  "ball",
  "area",
  "read",
  "lady"
]

Output:
false

Explanation:
The third row reads "read" while the third column reads "lead".

Therefore, it is NOT a valid word square.
Hide Company Tags Google
Show Similar Problems

"""
# My Solution
class Solution1(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        for row in range(len(words)):
            word = ''
            for trow in range(len(words)):
                if row < len(words[trow]):
                    word += words[trow][row]
                else:
                    break
            if words[row] != word:
                return False

        return True

# Looked up Solution
"""
>>> kk = ["abcde", "abcd", "abc", "ab", "a"]

>>> map(None, kk)
['abcde', 'abcd', 'abc', 'ab', 'a']

>>> map(None, *kk)
[('a', 'a', 'a', 'a', 'a'), ('b', 'b', 'b', 'b', None), ('c', 'c', 'c', None, None), ('d', 'd', None, None, None), ('e', None, None, None, None)]

>>> map(None, *map(None, *kk))
[('a', 'b', 'c', 'd', 'e'), ('a', 'b', 'c', 'd', None), ('a', 'b', 'c', None, None), ('a', 'b', None, None, None), ('a', None, None, None, None)]
>>>
"""

class Solution2(object):
    def validWordSquare(self, words):
        return map(None, *words) == map(None, *map(None, *words))

