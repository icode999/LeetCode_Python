"""
Find Duplicates in a phone number

Given a phone number. Check whether it is unique or not(ie no duplicates)

Companies
Amazon
"""
class Solution(object):
    def FindDupsPhoneNumber(self, number):
        """
        :param number: list of 10 nums (0-9)
        :return: True or False
        """
        i = 0
        while i < len(number):

            index = abs(number[i])
            if number[index] < 0:
                return False

            number[index] *= -1
            i += 1

        return True

numbers = [[1, 2, 3, 4, 5 ,6 ,7 ,8, 9, 0], [0, 1 , 5, 3, 2, 1, 5, 6, 7, 9], [1, 0, 5, 8, 7, 3, 2, 6, 3, 4],
           [1, 4, 5, 8, 7, 3, 2, 6, 9, 0]]

ss = Solution()
for num in numbers:
    print num, ss.FindDupsPhoneNumber(num)
