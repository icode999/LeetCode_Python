"""
443. String Compression

Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.


Follow up:
Could you solve it using only O(1) extra space?


Example 1:
Input:
["a","a","b","b","c","c","c"]

Output:
Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

Explanation:
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
Example 2:
Input:
["a"]

Output:
Return 1, and the first 1 characters of the input array should be: ["a"]

Explanation:
Nothing is replaced.
Example 3:
Input:
["a","b","b","b","b","b","b","b","b","b","b","b","b"]

Output:
Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].

Explanation:
Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
Notice each digit has it's own entry in the array.
Note:
All characters have an ASCII value in [35, 126].
1 <= len(chars) <= 1000.

Companies 
Microsoft Bloomberg Snapchat Yelp Expedia GoDaddy Lyft 

"""
# MOWN solution using 2 pointers
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if len(chars) < 2:
            return len(chars)

        def update_chars(current_char, pos, count):
            chars[pos] = current_char
            pos += 1

            if count > 1:
                for char in str(count):
                    chars[pos] = char
                    pos += 1

            return pos

        start, current_char, count = 0, chars[0], 1
        for i in range(1, len(chars)):
            if chars[i] == current_char:
                count += 1

            else:
                start = update_chars(current_char, start, count)
                current_char = chars[i]
                count = 1

        start = update_chars(current_char, start, count)
        return start

# same logic
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if len(chars) < 2:
            return len(chars)

        def update_chars(current_char, pos, count):
            chars[pos] = current_char
            pos += 1

            if count > 1:
                for char in str(count):
                    chars[pos] = char
                    pos += 1

            return pos

        start, current_char, count = 0, chars[0], 1
        for i in range(1, len(chars) + 1):
            if i == len(chars) or (chars[i] != current_char):
                start = update_chars(current_char, start, count)
                if i != len(chars):
                    current_char = chars[i]
                count = 1

            else:
                count += 1

        return start
