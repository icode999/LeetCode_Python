"""
917. Reverse Only Letters

Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place,
and all letters reverse their positions.
Example 1:

Input: "ab-cd"
Output: "dc-ba"
Example 2:

Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"


Note:

S.length <= 100
33 <= S[i].ASCIIcode <= 122
S doesn't contain \ or "

"""
import re
class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        if not S:
            return S

        S = list(S)
        low, high = 0, len(S) - 1
        while low < high:
            for i in range(low, high + 1):
                if re.search("[a-zA-Z]", S[i]):
                    low = i
                    break
            else:
                break

            for j in range(high, low - 1, -1):
                if re.search("[a-zA-Z]", S[j]):
                    high = j
                    break
            else:
                break

            S[low], S[high] = S[high], S[low]
            low += 1
            high -= 1

        return "".join(S)