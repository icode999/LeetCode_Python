"""
Given a rows x cols screen and a sentence represented by a list of non-empty words, find how many times the given sentence can be fitted on the screen.

Note:

A word cannot be split into two lines.
The order of words in the sentence must remain unchanged.
Two consecutive words in a line must be separated by a single space.
Total words in the sentence won't exceed 100.
Length of each word is greater than 0 and won't exceed 10.
1 <= rows, cols <= 20,000.
Example 1:

Input:
rows = 2, cols = 8, sentence = ["hello", "world"]

Output:
1

Explanation:
hello---
world---

The character '-' signifies an empty space on the screen.
Example 2:

Input:
rows = 3, cols = 6, sentence = ["a", "bcd", "e"]

Output:
2

Explanation:
a-bcd-
e-a---
bcd-e-

The character '-' signifies an empty space on the screen.
Example 3:

Input:
rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"]

Output:
1

Explanation:
I-had
apple
pie-I
had--

The character '-' signifies an empty space on the screen.
Hide Company Tags Google
Show Tags

"""

# got TLE without DP
"""
["try","to","be","better"]
10000
9001
"""
# My solution
class Solution1(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        result = 0
        counter_s = 0
        k = cols
        # rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"]
        for i in range(rows):
            while k >= len(sentence[counter_s]):
                k -= len(sentence[counter_s])
                counter_s += 1
                if k:
                    k -= 1
                else:
                    break

                if counter_s >= len(sentence):
                    counter_s = 0
                    result += 1

            if counter_s >= len(sentence):
                counter_s = 0
                result += 1
            k = cols

        return result


# Looked Up solution
# https://discuss.leetcode.com/topic/62455/21ms-18-lines-java-solution/2

class Solution2(object):
    def wordsTyping(self, sentence, rows, cols):
        string = " ".join(sentence) + " "   # join all the words into one stirng
        start, lens = 0, len(string)

        for i in range(rows):
            start += cols
            if string[start % lens] == " ":
                start += 1
            else:
                while start > 0 and string[(start-1) % lens] != " ":
                    start -= 1
        return start/lens




