"""
93. Restore IP Addresses

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)

"""
# Solution: Backtrack, base case is iter == 1 and int(string) < 256
# MOWN but with bugs
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s:
            return list()

        return self.Helper(s, 4)

    def Helper(self, string, iter):
        if not string:
            return None

        if iter == 1 and int(string) < 256:
            if str(int(string)) != string:  # Bug for the case "010010"
                return None

            return [string]

        elif iter == 1 and int(string) > 255:
            return None

        result = list()
        for i in range(len(string)):
            if string[0] == '0' and i > 0:  # Bug for the case "010010"
                break

            if int(string[:i + 1]) < 256:
                tresult = self.Helper(string[i + 1:], iter - 1)
                if tresult:
                    for res in tresult:
                        result.append(string[:i + 1] + '.' + res)
            else:
                break

        return result
