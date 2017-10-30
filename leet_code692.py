"""
692. Top K Frequent Words

Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
Note:
You may assume k is always valid, 1 <= k <= number of unique elements.
Input words contain only lowercase letters.
Follow up:
Try to solve it in O(n log k) time and O(n) extra space.

"""

from collections import defaultdict
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        words_map = defaultdict(int)
        for word in words:
            words_map[word] += 1

        count_list = defaultdict(list)
        for word, count in words_map.iteritems():
            count_list[count].append(word)

        keys = count_list.keys()
        keys.sort(reverse=True)
        counter = k

        result = list()
        for key in keys:
            count_list[key].sort()  # bug (need to sort, as we want alphabetically least )
            if len(count_list[key]) < counter:
                result += count_list[key][:]
                counter -= len(count_list[key])

            else:
                result += count_list[key][:counter]
                counter = 0

            if not counter:
                break

        return result
