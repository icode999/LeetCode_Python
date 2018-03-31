"""
781. Rabbits in Forest

In a forest, each rabbit has some color. Some subset of rabbits (possibly all of them) tell you how many other rabbits have the same color as them. Those answers are placed in an array.

Return the minimum number of rabbits that could be in the forest.

Examples:
Input: answers = [1, 1, 2]
Output: 5
Explanation:
The two rabbits that answered "1" could both be the same color, say red.
The rabbit than answered "2" can't be red or the answers would be inconsistent.
Say the rabbit that answered "2" was blue.
Then there should be 2 other blue rabbits in the forest that didn't answer into the array.
The smallest possible number of rabbits in the forest is therefore 5: 3 that answered plus 2 that didn't.

Input: answers = [10, 10, 10]
Output: 11

Input: answers = []
Output: 0
Note:

answers will have length at most 1000.
Each answers[i] will be an integer in the range [0, 999].

Companies
Wish


"""
class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        result, mapr = 0, dict()
        for num in answers:
            # if num is 0, that means there no other rabits of that color, so we add 1
            if num == 0:
                result += 1

            else:
                if num not in mapr:
                    # this particular color is not asked so far, so we add num (for others) and 1 for that rabit
                    mapr[num] = 1
                    result += num + 1
                else:
                    mapr[num] += 1
                    # check if mapr[num] exceeds num that means there are other colors with the same count
                    # for example [1, 1, 1] --> this means that there is red color rabits 2 and 1 blue color
                    # [1, 1] --> means that there are 2 red color rabits
                    if mapr[num] > num:
                        mapr.pop(num)

        return result
