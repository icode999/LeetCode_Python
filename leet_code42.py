"""
42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Hide Company Tags Google Twitter Zenefits Amazon Apple Bloomberg
Hide Tags Array Stack Two Pointers
Hide Similar Problems (M) Container With Most Water (M) Product of Array Except Self (H) Trapping Rain Water II

"""
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = leftID = 0
        right = rightID = len(height)-1
        result = 0

        while rightID > leftID:
            if height[left] <= height[right]:
                leftID += 1
                if height[left] > height[leftID]:
                    result += height[left]-height[leftID]

                else:
                    left = leftID

            else:
                rightID -= 1
                if height[right] > height[rightID]:
                    result += height[right]-height[rightID]

                else:
                    right = rightID

        return result