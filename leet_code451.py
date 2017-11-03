"""
451. Sort Characters By Frequency

Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

"""

from collections import defaultdict

# MOWN
# Solution: two dict, one for char: freq and second one for freq: [chars] and sort second dict keys and append
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        char_frequency = defaultdict(int)
        frequency_char = defaultdict(list)

        for char in s:
            char_frequency[char] += 1

        for char, freq in char_frequency.iteritems():
            frequency_char[freq].append(char * freq)

        result = ''
        keys = frequency_char.keys()
        keys.sort(reverse=True)

        for key in keys:
            result += ''.join(frequency_char[key])

        return result